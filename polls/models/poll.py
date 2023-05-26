from django.db import models

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