from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

import datetime
# Create your models here.
class Question(models.Model):

    question_text = models.CharField(
        max_length = 200,
        blank=False, 
        null=True,
        verbose_name="question"
    )

    pub_date = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="date published"
    )

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse_lazy('polls:question_detail', args=[self.pk])
    class Meta:
        ordering = ['pub_date']
        verbose_name = "question"
        verbose_name_plural = "questions"
    
class Choice(models.Model):

    question = models.ForeignKey(
        Question,
        db_index=True, 
        editable=True,
        on_delete=models.CASCADE,
        verbose_name="question choice"
    )

    choice_text = models.CharField(
        max_length = 200,
        blank=False, 
        null=True,
        verbose_name="choice"
    )

    votes = models.IntegerField(
        default=0,
        verbose_name="votes cast"
    )

    class Meta:
        ordering = ['choice_text']
        verbose_name = "choice"
        verbose_name_plural = "choices"