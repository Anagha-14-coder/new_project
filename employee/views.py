from django.shortcuts import render
from employee.models import employee_db
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeView(APIView):
    def get(self, request):
        # Retrieve all employee objects
        employi = employee_db.objects.all()
        serializer = EmployeeSerializer(employi, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Create a new employee object
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        # Update an existing employee object
        try:
            employi = employi.objects.get(id=request.data['id'])
        except employi.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employi, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        # Delete a employee object
        try:
            employi = employi.objects.get(id=request.data['id'])
        except employi.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employi.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
