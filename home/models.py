from django.db import models
from login.models import User

# Create your models here.
class Travel(models.Model):
    planned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    destination = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    df = models.DateTimeField() # date from
    dt = models.DateTimeField() # date to
    join = models.ManyToManyField(User, through='Join')

class Join(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_id = models.ForeignKey(Travel, on_delete=models.CASCADE)
    join_at = models.DateTimeField(auto_now_add=True)
 
