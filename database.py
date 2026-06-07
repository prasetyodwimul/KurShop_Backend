from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# ================================
# KONFIGURASI DATABASE
# ================================

DATABASE_URL = "mysql+pymysql://root:@localhost/kurshop"


# ================================
# ENGINE DATABASE
# ================================ 

engine = create_engine(DATABASE_URL)


# ================================
# SESSION DATABASE
# ================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ================================
# BASE MODEL
# ================================

Base = declarative_base()


# ================================
# DEPENDENCY DATABASE
# ================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()