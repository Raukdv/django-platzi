#django modules
from django.urls import include, path

#project modules
from polls import views

#Patterns
urlpatterns = [
    #Home Patterns
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    #Detail Pattern
    path(
        'detail/<int:pk>/',
        views.DetailView.as_view(),
        name='question_detail'
    ),
    #Vote Pattern
    path(
        'vote/<int:question_id>/',
        views.vote,
        name='vote'
    ),
    #Results Pattern
    path(
        'results/<int:pk>/',
        views.ResultsView.as_view(),
        name='results'
    ),
]