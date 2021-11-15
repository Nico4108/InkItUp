from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from api.models import Tattooparlor as Tattooparlor

# Create your models here.
class User(AbstractUser, models.Model):    
    Tattooparlor_cvr = models.ForeignKey(Tattooparlor, on_delete=models.CASCADE, db_column='Tattooparlor_CVR')  # Field name made lowercase.

    REQUIRED_FIELDS = ['email', 'Tattooparlor_cvr']
    
    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'User'