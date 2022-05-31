from rest_framework import serializers
from .models import (
    School,
    Student,
)
from .utils.utils import (
    sanitize_name,
    name_isvalid,
    school_name_isvalid,
)

class SchoolSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        """
        Validate names of schools
        """
        if not school_name_isvalid(value):
            raise serializers.ValidationError("Invalid name")
        return sanitize_name(value)
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        """
        Validate names of student's first_name and last_name
        """
        if not name_isvalid(value):
            raise serializers.ValidationError("Invalid name")
        return sanitize_name(value)
    class Meta:
        model = Student
        fields = '__all__'
