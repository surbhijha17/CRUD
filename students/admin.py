from django.contrib import admin
from .models import Student
#admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','rollno','classinfo','mobileno')
admin.site.register(Student, StudentAdmin)
