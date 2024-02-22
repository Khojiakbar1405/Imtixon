from django.db import models

# Xodimlar saqlanadi
class Employees(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.l_name
    

# Davomat yoziladi
class Attendance(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=1)
    attendancedate = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return str(self.employee)
