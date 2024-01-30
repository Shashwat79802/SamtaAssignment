from django.db import models


class Student(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=20)
    last_name = models.CharField(verbose_name='Last Name', max_length=20)
    age = models.IntegerField(verbose_name='Age')
    grade = models.IntegerField(verbose_name='Grade')

    def __str__(self):
        return self.name