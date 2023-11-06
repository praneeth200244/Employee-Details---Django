# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>HOME PAGE</h1>')

from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    # print(employees)
    context = {
        'employees':employees
    }
    return render(request, 'home.html', context)