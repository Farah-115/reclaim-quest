from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# هذا هو رابط قاعدة البيانات (رح يعمل ملف اسمه project.db جوا مجلدك)
SQLALCHEMY_DATABASE_URL = "sqlite:///./project.db"

# إنشاء المحرك اللي بيتواصل مع قاعدة البيانات
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# إنشاء الجلسة اللي رح نستخدمها لإضافة أو سحب البيانات
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# الأساس اللي رح نبني عليه جداول قاعدة البيانات (Models)
Base = declarative_base()