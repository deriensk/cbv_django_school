from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

class CVView(View):

    def get(self, request):
        return HttpResponse("WE ARE USING CLASS BASED VIEWS NOW")

class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['my_key'] = 'I am the value of that key'
        return context
         


def index(request):

    context = {}
    return render(request, 'index.html', context)

class SchoolListView(ListView):

    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):

    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'