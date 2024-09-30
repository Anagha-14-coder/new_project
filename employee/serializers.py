from rest_framework import serializers
from .models import employee_db

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_db  # Specify the model to be serialized
        fields = ['id', 'employee_name', 'employee_category', 'employee_phone', 'employee_dob',
                  'employee_gender', 'employee_address', 'employee_email', 'employee_qualification' ]  # Specify the fields to be included in the serialized output