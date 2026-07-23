from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    # Primary key. Integer identity columns are the simplest, most portable
    # choice for a primary key and are indexed automatically by Postgres.
    id: Mapped[int] = mapped_column(primary_key=True)

    # The user's email address, used as their login identifier. unique=True
    # adds a database-level uniqueness constraint so two users can never
    # share an email, even under concurrent inserts. index=True speeds up
    # the lookups this column will constantly be queried by (e.g. login).
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    # The user's display name. A plain, non-unique string -- there's no
    # business rule requiring full names to be distinct.
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Whether the account is active. Modeled as a real column (rather than
    # deleting the row) so accounts can be disabled without losing data,
    # and defaults to True so newly created users are active by default.
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)