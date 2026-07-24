from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


# Routes are intentionally thin. This function's only jobs are:
# validate the request (handled automatically by the UserCreate type
# hint), call the one service method that does the real work, and
# translate whatever comes back into an HTTP response. It contains no
# business rules of its own -- "is this email already taken?" and "how
# do we hash a password?" are questions this function doesn't even know
# how to ask. That logic lives in AuthService, where it can be reused
# (e.g. by a future admin-created-user flow) and unit tested without
# spinning up HTTP at all. If this function ever grows an `if` statement
# that isn't about status codes, that's a signal the logic belongs one
# layer down instead.
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    auth_service = AuthService(db)

    try:
        return auth_service.register(user_data)
    except ValueError as exc:
        # The service layer raises plain ValueError because it has no
        # concept of HTTP -- it's reusable outside a web context. The
        # API layer's job is to translate that domain-level error into
        # something HTTP clients understand: a 400 response with a
        # useful message.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc