from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """
    Schema for incoming registration requests.

    This is what a client sends to us -- it includes the plaintext
    password because that's the only way a password can arrive at the
    API in the first place. The password never touches the database in
    this form; the service layer will hash it (via app/core/security.py)
    before it's ever persisted. This schema's job ends the moment that
    hashing happens.
    """

    email: EmailStr = Field(..., description="The user's email address")
    full_name: str = Field(..., min_length=2, max_length=255)
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    """
    Schema for outgoing user data returned by the API.

    Notice there is no `password` field here at all -- not hashed, not
    plaintext, not anything. This is intentional and important: even a
    bcrypt hash should never be sent back to a client. It's not needed
    for anything on the client side, and exposing it unnecessarily
    increases the damage if a response is ever logged, cached, or
    intercepted somewhere it shouldn't be. The rule is simple: a field
    should only appear in a response schema if the client genuinely
    needs it.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str
    is_active: bool