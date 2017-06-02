from django.db import models
from django.core.validators import int_list_validator

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    screen_name = models.CharField(max_length=15)
    oauth_key = models.CharField(max_length=100)
    oauth_secret = models.CharField(max_length=100)
    blocked_user_ids=models.TextField(validators=[int_list_validator], default='')
