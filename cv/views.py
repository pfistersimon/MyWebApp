from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from cv.forms import ExperienceForm

from .models import Mycv, Experience, Education
# Create your views here.
class IndexView(generic.ListView):
    template_name = "cv/index.html"
    context_object_name = "experiences_list"

    def get_queryset(self):
        cv = Mycv.objects.get(id=Mycv.DEFAULT_ID_CV)
        return cv.experience_set.all() 
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        cv = Mycv.objects.get(id=Mycv.DEFAULT_ID_CV)
        context['educations_list'] = cv.education_set.all() 
        return context

class ExperienceDetailView(generic.DetailView):
    model = Experience
    template_name='cv/experience_detail.html'
    context_object_name = 'experience'

class EducationDetailView(generic.DetailView):
    model = Education
    template_name='cv/education_detail.html'
    context_object_name = 'education'

class ExperienceCreate(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'cv/experience_form.html'

class ExperienceUpdate(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'cv/experience_form.html'
    
class ExperienceDelete(DeleteView):
    model = Experience
    success_url = reverse_lazy('cv:index')

def index (request):
    return render(request, 'cv/index.html', context=None, content_type=None, status=None, using=None)
