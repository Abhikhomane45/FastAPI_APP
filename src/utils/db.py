from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.utils.settings import settings

engine=create_engine(
    url=settings.DB_CONNECTION
)

LocalSession=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
    )

# Base class for database models
Base = declarative_base()


# Provide a database session to FastAPI
def get_db():
    session = LocalSession()

    try:
        yield session
    finally:
        session.close()
