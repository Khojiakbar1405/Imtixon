import views 
from django.urls import path


urlpatterns = [
    path('staff-create/', views.staff_create),
    path('staf-list/', views.staff_list),
    path('attendance-create/', views.attendance_create),
    path('attendance-day/', views.attendance_day),
    path('attendance-month/', views.attendance_month),
    path('attendance-week/', views.attendance_week),
]