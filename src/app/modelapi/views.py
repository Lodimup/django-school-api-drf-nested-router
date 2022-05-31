from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import (
    School,
    Student,
)
from .serializers import (
    SchoolSerializer,
    StudentSerializer,
)

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
        Overrides the default get_queryset to filter of /schools/<school_id>/students/<pk> for conditions where values are/ are not provided
        self.kwargs is a dictionary of all the kwargs passed to the view by router
        """
        # filter by first_name support on all student routes
        if self.request.query_params.get('first_name', None) != None:
            return Student.objects.filter(first_name=self.request.query_params.get('first_name'))
        # filter by last_name support on all student routes
        if self.request.query_params.get('last_name', None) != None:
            return Student.objects.filter(first_name=self.request.query_params.get('first_name'))

        # build query
        school_id = self.kwargs.get('schools_pk', None)
        student_id = self.kwargs.get('pk', None)
        query = {
            'school': school_id,
            'id': student_id
        }
        # remove query with value None
        query = {k: v for k, v in query.items() if v is not None}
        # if no query is given, return all students
        if len(query) == 0:
            return self.queryset.all()

        return Student.objects.filter(**query)

    def perform_create(self, serializer):
        """
        Overrides the default perform_create to
        satisfies condition in step 2: disallow addition of a student if the school is full
        """
        max_student = serializer.validated_data['school'].max_student
        if Student.objects.filter(school=serializer.validated_data['school']).count() >= max_student:
            raise ValidationError('School is full')
        serializer.save()

    def perform_update(self, serializer):
        if serializer.validated_data.get('school', None) != None: # Accounts for patch without school id/ object
            max_student = serializer.validated_data['school'].max_student
            print(Student.objects.filter(school=serializer.validated_data['school']).count())
            if Student.objects.filter(school=serializer.validated_data['school']).count() >= max_student:
                raise ValidationError('School is full')
        serializer.save()

