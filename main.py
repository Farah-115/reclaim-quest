from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas

# إنشاء الجداول إذا مش موجودة
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# دالة عشان تفتح اتصال مع قاعدة البيانات لكل طلب، وتسكره بس يخلص
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working with the Database!"}

@app.get("/users/{user_id}/report")
def get_user_report(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"error": "المستخدم غير موجود"}

    last_score = db.query(models.Score).filter(models.Score.user_id == user_id).order_by(models.Score.id.desc()).first()
    
    if not last_score:
        return {"message": f"أهلاً {user.name}، لا يوجد لديك أي نتائج حتى الآن."}

    score_val = last_score.freedom_score
    
    # 3. تجهيز الطلب (Prompt) للذكاء الاصطناعي
    prompt = f"اللاعب {user.name} حصل على نتيجة {score_val} من 100 في مقياس Freedom Score. أعطه نصيحة ذكية، مفيدة، وتشجيعية قصيرة جداً (سطرين كحد أقصى) باللغة العربية بناءً على نتيجته."
    
    # 4. إرسال الطلب لـ Gemini واستقبال الرد
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        ai_recommendation = response.text
    except Exception as e:
        # هون رح نطبع الخطأ الحقيقي عشان نقدر نقرأه
        print(f"Gemini Error: {str(e)}") 
        ai_recommendation = f"تفاصيل الخطأ: {str(e)}"
    return {
        "player_name": user.name,
        "email": user.email,
        "latest_freedom_score": score_val,
        "ai_recommendation": ai_recommendation
    }
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas
from google import genai # <--- أضفنا هاي

# حط المفتاح السري تبعك هون (استبدل YOUR_API_KEY بالرمز اللي نسخته)
client = genai.Client(api_key="api-key-slot-1") 

# ... باقي الكود (إنشاء الجداول والدالة get_db)