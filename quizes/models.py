from django.db import models
import random

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='продолжительность теста в минутах')
    required_score_to_pass = models.IntegerField(help_text='проходной балл %')

    def __str__(self):
        return self.name

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions

    class Meta:
        verbose_name_plural = 'Quizes'
