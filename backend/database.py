from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./legalese.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text)
    plain_translation = Column(Text)
    red_flags = Column(Text)  # JSON string of flags
    risk_score = Column(Integer)
    summary = Column(Text)
    clauses = Column(Text)  # JSON string of clause breakdown

Base.metadata.create_all(bind=engine)