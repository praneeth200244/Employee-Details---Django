from django.shortcuts import get_object_or_404, render
from employees.models import Employee
from django.http import Http404, HttpResponse

# Create your views here.
def employeeDetails(request, pk):
    # try:
    #     employee = Employee.objects.get(pk = pk)
    # except:
    #     raise Http404
    employee = get_object_or_404(Employee, pk=pk)
    # return HttpResponse(employee)
    context = {
        'employee':employee
    }
    return render(request, 'employeeDetail.html', context)