from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate


class AuthService:
    """
    Business logic for authentication-related operations.

    This is where rules like "an email can only be registered once" or
    "passwords must be hashed before storage" live -- rules that aren't
    about HTTP (that's the API layer's job) and aren't about SQL syntax
    (that's the repository's job). They're decisions about how the
    application is allowed to behave.
    """

    def __init__(self, db: Session) -> None:
        self.db = db
        # The service owns the repository, not the other way around.
        # Routes and other callers only ever talk to AuthService -- they
        # never need to know a UserRepository exists at all.
        self.user_repo = UserRepository(db)

    def register(self, user_data: UserCreate) -> User:
        """
        Register a new user.

        Raises:
            ValueError: if a user with this email already exists.
        """
        existing_user = self.user_repo.get_by_email(user_data.email)
        if existing_user is not None:
            raise ValueError("Email already registered")

        # Hashing happens here, in the service layer, not in the
        # repository, for two reasons:
        #
        # 1. The repository's job is persistence -- turning data into
        #    rows -- not deciding how that data should be transformed
        #    first. Hashing is a security policy decision, and policy
        #    decisions belong in the service layer, where the rest of
        #    your business rules already live.
        #
        # 2. It keeps the repository reusable and honest about its
        #    inputs. UserRepository.create() takes a hashed_password
        #    and does exactly what it's told -- it never silently
        #    hashes a plaintext value for you. That means the
        #    repository can never be the thing that "forgets" to hash a
        #    password; whoever calls it is responsible for handing it
        #    the right thing, and that responsibility is visible right
        #    here, in one place, instead of hidden a layer down.
        hashed_password = hash_password(user_data.password)

        return self.user_repo.create(
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
        )