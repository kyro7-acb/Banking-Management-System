from django.db import models

# Create your models here.

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    # Add other branch fields as necessary
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.branch_name

class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    c_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='customers')
    c_name = models.CharField(max_length=50)
    c_address = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    c_phone = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.c_name
