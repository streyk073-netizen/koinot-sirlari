# views.py - O'rganish va Viktorina tizimi
from django.shortcuts import render
from django.http import JsonResponse


# Bu yerga AI API kutubxonasini ulaymiz (masalan, google-generativeai yoki openai)

# 1. Bosh sahifa (Ikkita katta neon tugma bilan)
def home_page(request):
    return render(request, 'index.html')


# 2. O'rganish bo'limi (AI matn generatsiyasi)
def learn_space(request):
    topic = request.GET.get('topic', 'Qora tuynuklar')  # Standart mavzu

    # AI-ga yuboriladigan maxsus xavfsiz prompt
    ai_prompt = f"Koinot haqidagi {topic} mavzusida eng qiziqarli, noyob va ilmiy faktlarni sodda tilda yozib ber."

    # AI javobini olish logikasi (Bu yerda API chaqiriladi)
    # ai_response = ai_model.generate_content(ai_prompt)
    ai_text = "AI tomonidan generatsiya qilingan koinot sirlari matni..."  # Vaqtincha

    return render(request, 'learn.html', {'topic': topic, 'content': ai_text})


# 3. Viktorina darajalari bo'limi
def quiz_levels(request):
    # Bazadan barcha bosqichlarni olamiz (Quyosh tizimi, Yulduzlar, Qora tuynuklar)
    # levels = QuizLevel.objects.all().order_by('order')
    return render(request, 'quiz_levels.html')
