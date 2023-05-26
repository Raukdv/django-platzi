#django modules
from django.urls import include, path

#project modules
from polls import views

#Patterns
urlpatterns = [
    #Home Patterns
    path(
        '',
        views.index,
        name='index'
    ),
]