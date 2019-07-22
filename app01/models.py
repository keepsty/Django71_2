from django.db import models


# Create your models here.


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Dept(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=32)

    def __str__(self):
        return self.dept_name
