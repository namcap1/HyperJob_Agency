from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from resume.forms import NewResumeForm
from vacancy.forms import NewVacancyForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username,
        }
        return render(request, 'menu.html', context=context)

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = NewVacancyForm() if request.user.is_staff else NewResumeForm()
        context = {
            'form': form,
            'is_authenticated': request.user.is_authenticated,
            'is_staff': request.user.is_staff,
            'username': request.user.username,
        }
        return render(request, 'home.html', context=context)
