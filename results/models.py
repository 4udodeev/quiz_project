from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self) -> str:
        return f'{self.user.last_name} {self.user.first_name} - {self.quiz.name}'
