from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views import View

from .forms import NewResumeForm
from .models import Resume
# Create your views here.
class resume_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resumes.html', context={'resumes': Resume.objects.all()})

class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        can_submit = request.user.is_authenticated and not request.user.is_staff
        if not can_submit:
            raise PermissionDenied

        form = NewResumeForm(request.POST)
        if not form.is_valid():
            return redirect('/home')

        author = request.user
        description = form.cleaned_data['description']
        Resume.objects.create(author=author, description=description)
        return redirect('/home')
