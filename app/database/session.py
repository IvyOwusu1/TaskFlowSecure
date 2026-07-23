from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# --------------------------------------------------------------------------
# Engine
# --------------------------------------------------------------------------
# The engine is the starting point for any SQLAlchemy application. It holds
# the connection pool to the database and knows how to speak the specific
# SQL dialect (PostgreSQL, in this case). It is created exactly once, at
# import time, and reused for the lifetime of the application.
engine = create_engine(settings.DATABASE_URL)

# --------------------------------------------------------------------------
# Session factory
# --------------------------------------------------------------------------
# SessionLocal is not a session itself -- it is a factory that produces new
# Session objects on demand. A Session is the object you actually use to
# run queries and commit transactions. We configure the factory once here
# so every part of the app creates sessions the same, consistent way.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# --------------------------------------------------------------------------
# Dependency
# --------------------------------------------------------------------------
# get_db() is a generator function used as a FastAPI dependency. FastAPI
# calls it before the route runs, injects the yielded session into the
# route via Depends(get_db), and resumes the function after the route
# finishes to run the cleanup code. This guarantees the session is always
# closed, even if the route raises an exception.
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()