from django.contrib import admin

# Register your models here.
from .models import (
    School,
    Student,
)

# Register your models here.
# Use inline here for ease of manually inputting data
class StudentInline(admin.StackedInline):
    """
    This section generates /admin/ view for easy debug and manual entry.
    Serializer check is NOT enforced
    """
    model = Student
    extra = 0

class SchoolInline(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(School, SchoolInline)
admin.site.register(Student)
