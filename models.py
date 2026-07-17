from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 1. جدول المستخدمين (User Model)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    # ربط المستخدم بالنقاط (Scores) تبعته
    scores = relationship("Score", back_populates="owner")

# 2. جدول السيناريوهات (Scenario Model)
class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

# 3. جدول النقاط (Score Model)
class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    freedom_score = Column(Float, default=0.0)
    
    # ربط النتيجة بمستخدم معين عن طريق الـ ID
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="scores")