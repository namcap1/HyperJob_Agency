from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views import View
from .forms import NewVacancyForm
from .models import Vacancy
# Create your views here.

class vacancy_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})

class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        can_submit = request.user.is_authenticated and request.user.is_staff
        if not can_submit:
            raise PermissionDenied

        form = NewVacancyForm(request.POST)
        if not form.is_valid():
            return redirect('/home')

        author = request.user
        description = form.cleaned_data['description']
        Vacancy.objects.create(author=author, description=description)
        return redirect('/home')


