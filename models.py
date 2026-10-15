from django.db import models
from django.contrib.auth.models import User

# 1. Viktorina Bosqichlari (Masalan: 1-Quyosh tizimi, 2-Yulduzlar, 3-Qora tuynuklar)
class QuizLevel(models.Model):
    title = models.CharField(max_length=150)
    order = models.IntegerField(unique=True) # Bosqich tartibi (1, 2, 3...)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.order}-Bosqich: {self.title}"

# 2. Kosmik Savollar Modeli
class SpaceQuestion(models.Model):
    level = models.ForeignKey(QuizLevel, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    # Kiberxavfsizlik uchun: To'g'ri javob shifrlangan yoki faqat backend biladigan harf ko'rinishida saqlanadi
    correct_option = models.CharField(max_length=1) # 'A', 'B', 'C', 'D'

    def __str__(self):
        return f"[{self.level.title}] {self.question_text[:40]}..."

# 3. Foydalanuvchining Profili va Erishgan Natijalari
class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=1) # Foydalanuvchi hozir qaysi bosqichda
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} — {self.current_level}-bosqichda"
