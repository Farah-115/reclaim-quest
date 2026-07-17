from pydantic import BaseModel

# القالب اللي رح نستخدمه لما نستقبل بيانات من المستخدم عشان نسجله
class UserCreate(BaseModel):
    name: str
    email: str

# القالب اللي رح نرجعه للمستخدم بعد ما يتسجل بنجاح (بيشمل الـ ID)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
        # قالب استلام النتيجة من اللعبة
class ScoreCreate(BaseModel):
    freedom_score: float

# قالب إرجاع النتيجة بعد حفظها بقاعدة البيانات
class ScoreResponse(BaseModel):
    id: int
    freedom_score: float
    user_id: int

    class Config:
        from_attributes = True