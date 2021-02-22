from django.urls import path

from . import views

urlpatterns = [
    path('', views.resume_index.as_view()),
    path('/new', views.NewResumeView.as_view()),
]
