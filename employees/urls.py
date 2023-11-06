from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.employeeDetails, name='employee_detail')
]
