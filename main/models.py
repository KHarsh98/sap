from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length = 100, null=True)
    designation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    
