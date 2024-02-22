from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from . import serializers
from api import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Xodimlar ro`yxati`
@api_view('GET')
def staff_list(request):
    employee = models.Employees.objects.all()
    serializer = serializers.ListEmployeesSerializer(employee, many=True)
    return Response(serializer.data)



# davomat yaratiladi
@api_view('POST')
def attendance_create(request, id):
    ...
    return Response('')


# xodim yaratiladi
@api_view('POST', 'GET')
def staff_create(request):
    if request.method == 'GET':
        employee = models.Employees.objects.all()
        serializer = serializers.ListEmployeesSerializer(employee, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CreateEmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# davomatning kunlik ro`yxati`
@api_view('GET')
def attendance_day(request):
    attendance = models.Attendance.objects.all()
    serializer = serializers.ListAttendanceSerializer(attendance, many=True)
    return Response(serializer.data)


# davomatning haftalik ro`yxati`
@api_view('GET')
def attendance_week(request):
    attendance = models.Attendance.objects.all()
    serializer = serializers.ListAttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

# davomatning oylik ro`yxati`
@api_view('GET')
def attendance_month(request):
    attendance = models.Attendance.objects.all()
    serializer = serializers.ListAttendanceSerializer(attendance, many=True)
    return Response(serializer.data)
