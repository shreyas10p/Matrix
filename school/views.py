from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Students
from django.template import Context

# Create your views here.


class TableView(ListView):
    template_name = 'student/index.html'
    model = Students

    def get_context_data(self, **kwargs):
        student_data = Students.objects.all().order_by("created_on")
        print(student_data)
        context = super().get_context_data(**kwargs)
        context['student_data'] = student_data
        return context
