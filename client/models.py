from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.urls import reverse


class Client (models.Model):
    GENDER_CHOICES = (
        ('Active', 'Active'),
        ('not Active', 'not Active'),
    )
    Name = models.CharField(
        max_length=100, default="name")
    Mobile = models.CharField(
        max_length=225,  default="Mobile")
    Email = models.EmailField()
    Country = models.CharField(
        max_length=100, default="Country")
    City = models.CharField(
        max_length=100, default="City")
    Date_of_Birth = models.DateField()
    Contract_Start_Date = models.DateField()
    Contract_End_Date = models.DateField()
    Status = models.CharField(max_length=100, choices=GENDER_CHOICES)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('client_detail',args=[str(self.id)])

    def __str__(self):
       return self.Name


    class Meta:
        verbose_name_plural = "Clients"
        ordering=['-pk']
