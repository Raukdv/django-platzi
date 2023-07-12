from django.contrib import admin

# Register your models here.

#Models
from .models import Question, Choice


#Inlines
class ChoicesInline(admin.StackedInline):
    model = Choice
    can_delete = False
    verbose_name_plural = 'choices'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (
        ChoicesInline,
    )
    list_display = (
        'question_text',
    )
    search_fields = (
        'question_text',
    )
    ordering = (
        '-pub_date',
    )

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'choice_text',
    )
    search_fields = (
        'choice_text',
    )
    ordering = (
        '-votes',
    )