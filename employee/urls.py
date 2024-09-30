from django.urls import path
from employee.views import EmployeeView





urlpatterns = [
    
    path('Employees/', EmployeeView.as_view(), name='employee'),
    
]