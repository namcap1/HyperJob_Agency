from django.urls import path

from . import views

urlpatterns = [
    path('', views.vacancy_index.as_view()),
    path('/new', views.NewVacancyView.as_view()),
]
