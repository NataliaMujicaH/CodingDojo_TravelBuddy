from django.db import models
from login.models import User

class TravelManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(postData['destination']) == 0:
            errores['destination'] = "Destination is required"
        if len(postData['description']) == 0:
            errores['description'] = "Description is required"
        if len(postData['df']) == 0:
            errores['df'] = "Start date is required"
        if len(postData['dt']) == 0:
            errores['dt'] = "End date is required"
        return errores

# Create your models here.
class Travel(models.Model):
    planned_by = models.ForeignKey(User, related_name='planner')
    destination = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    df = models.DateTimeField() # date from
    dt = models.DateTimeField() # date to
    join_user = models.ForeignKey(User, related_name='joining_user')


 
