"""Models."""
from django.contrib.auth.models import User
from django.db import models

from quizes.models import Quiz


class Result(models.Model):
    """Результаты тестирования."""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self) -> str:
        """Str."""
        return (f'{self.user.last_name} {self.user.first_name} -'
                f' {self.quiz.name}')
