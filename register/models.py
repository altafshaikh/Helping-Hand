from django.db import models
from django.contrib import auth
from django.contrib.auth.models import Permission, User


BLOOD_GROUPS=(
('A+','A+'),
('A-','A-'),
('B+','B+'),
('B-','B-'),
('O+','O+'),
('O-','O-'),
('AB+','AB+'),
('AB-','AB-'),
)
class Doner(models.Model):
    doner= models.CharField(max_length = 250)
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUPS, default='black')
    mobile_no = models.CharField(max_length = 12)
    email = models.CharField(max_length = 250)
    city = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.doner)
