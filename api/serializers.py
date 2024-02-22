from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework import serializers
from api import models 


# Xodimlar serializeri  yani hamma malumotlar chiqadi
class ListEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = '__all__'


# Davomat serializeri  yani hamma malumotlar chiqadi
class ListAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'


# Davomat yaratish
class CreateEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ['f_name', 'l_name']

