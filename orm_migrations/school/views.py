from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student, Teacher
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {'object_list': Student.objects.order_by('name')}

    return render(request, template, context)
