from django.db import models
from django.contrib.auth.models import User

# Create your models here.
user = models.ForinKey(User,on_delete = models.CASCADE)
date = models.DateTimeFeild(auto_now_add = True)