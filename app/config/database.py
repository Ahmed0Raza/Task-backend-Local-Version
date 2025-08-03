from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:715396Ar@localhost/postgres"

# Create engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test connection
try:
    with engine.connect() as conn:
        print("✅ Connected to the database successfully.")
except OperationalError as e:
    print("❌ Failed to connect to the database.")
    print(f"Error: {e}")
