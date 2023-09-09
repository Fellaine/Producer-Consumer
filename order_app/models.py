from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.TextField(null=False, blank=False)


class Order(models.Model):
    task_id = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
