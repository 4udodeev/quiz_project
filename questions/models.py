from django.db import models
from quizes.models import Quiz
import random


class Question(models.Model):
    text = models.CharField(max_length=254)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_weight = models.IntegerField(help_text='Вес вопроса', default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

    def get_answers(self):
        answers = list(self.answer_set.all())
        random.shuffle(answers)
        return answers


class Answer(models.Model):
    text = models.CharField(max_length=254)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
