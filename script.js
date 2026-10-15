// Kosmik viktorina uchun xavfsiz va dinamik JS mantiqi

document.querySelectorAll('.option-btn').forEach(button => {
    button.addEventListener('click', function() {
        const questionId = this.dataset.questionId;
        const chosenOption = this.dataset.option; // 'A', 'B', 'C' yoki 'D'
        const quizCard = document.getElementById(`quiz-card-${questionId}`);

        // Xavfsizlik uchun: Django CSRF tokenini inputdan olamiz
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Backend-ga (Django-ga) xavfsiz POST so'rovi yuborish
        fetch('/check-answer/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `question_id=${questionId}&chosen_option=${chosenOption}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_correct) {
                // Javob to'g'ri bo'lsa - neon yashil chiroq va keyingi bosqichga o'tish
                this.classList.add('correct-glow');
                setTimeout(() => {
                    alert("Ajoyib! Koinot siri topildi. Keyingi savolga o'tamiz! 🌌");
                    window.location.reload(); // Sahifani yangilash (yangi savol chiqadi)
                }, 800);
            } else {
                // Javob noto'g'ri bo'lsa - Sizning "Sehrli to'p"ingiz kabi SHAKE effekti ishlaydi!
                quizCard.classList.add('wrong-answer-shake');
                this.classList.add('wrong-glow');

                // Animatsiya tugagandan keyin klassni olib tashlaymiz (qayta kliklash uchun)
                setTimeout(() => {
                    quizCard.classList.remove('wrong-answer-shake');
                }, 400);
            }
        })
        .catch(error => console.error('Xatolik yuz berdi:', error));
    });
});
