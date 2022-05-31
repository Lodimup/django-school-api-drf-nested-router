from django.contrib import admin

# Register your models here.
from .models import (
	School,
	Student,
)

# Register your models here.
# Use inline here for ease of manually inputting data
class StudentInline(admin.StackedInline):
	model = Student
	extra = 0

class SchoolInline(admin.ModelAdmin):
	inlines = [StudentInline]

admin.site.register(School, SchoolInline)
admin.site.register(Student)
