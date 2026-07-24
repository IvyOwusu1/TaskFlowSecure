from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Encapsulates all direct database access for the User model.

    Nothing outside this class should write raw SQLAlchemy queries
    against `User` -- services call these methods instead. That keeps
    query logic in one place, and means the service layer can be tested
    against a fake/mock repository without needing a real database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        """
        Look up a single user by email, or return None if no match.

        Uses SQLAlchemy 2.0's select() + scalar_one_or_none() pattern,
        which is the modern replacement for the old Query API. It
        returns exactly one User object (not a Row/tuple), or None if
        no row matched -- no exception is raised for a missing user,
        since "no such user" is an expected, normal outcome here, not
        an error condition.
        """
        statement = select(User).where(User.email == email)
        return self.db.execute(statement).scalar_one_or_none()

    def create(self, email: str, full_name: str, hashed_password: str) -> User:
        """
        Persist a new user and return the fully populated row.

        Note: this method takes hashed_password, not password -- hashing
        is deliberately not this layer's job (see class docstring). By
        the time this method is called, the caller has already hashed
        it.
        """
        user = User(
            email=email,
            full_name=full_name,
            hashed_password=hashed_password,
        )

        self.db.add(user)
        self.db.commit()

        # refresh() re-fetches the row's current state from the database
        # after the commit. This matters because the database, not
        # Python, is what actually generates the id (via auto-increment)
        # and applies any column defaults declared at the DB level. Right
        # after add()+commit(), the `user` object in memory doesn't yet
        # know its own id -- refresh() pulls that back so the object we
        # return to the caller is complete and accurate, not partially
        # populated.
        self.db.refresh(user)

        return user