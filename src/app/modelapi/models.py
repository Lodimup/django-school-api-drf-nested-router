from django.db import models
from .utils.utils import (
    gen_uuid,
)

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    max_student = models.PositiveBigIntegerField(default=1)  # safe up to 9223372036854775807

    def __str__(self):
        """
        For debugging purpose in admin view
        """
        return f'{self.id=} {self.name=} {self.max_student=}'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    unique_id = models.CharField(max_length=20, unique=True, default=gen_uuid)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        """
        For debugging purpose in admin view
        """
        return f'{self.id=} {self.school.name=} {self.first_name=} {self.last_name=} {self.unique_id=}'
