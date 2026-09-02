from products.models import Product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    historic_price = models.DecimalField(max_digits=10, decimal_places=2)