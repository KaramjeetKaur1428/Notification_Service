from sqlalchemy import Column, Integer, String, Text, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String, default='pending')  # pending, sent, failed

engine = create_engine("sqlite:///notifications.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
