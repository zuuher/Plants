from django.db import models

# Create your models here.
class Plant(models.Model):
   name=models.CharField(max_length=100)
   price=models.FloatField()
   life_cycle=models.CharField(max_length=100)
   old=models.IntegerField()
   image=models.ImageField(upload_to='images/')
   plan_id=models.AutoField(primary_key=True)
   def __str__(self):
        return self.name
   
class user(models.Model):
    # use a string primary key so user_id can be a name instead of a number
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model): 
    total_price=models.FloatField()
    order_status=models.CharField(max_length=100)
    Order_date=models.DateField(auto_now_add=True)


class category(models.Model):
    tree=models.CharField(max_length=100)
    shrub=models.CharField(max_length=100)
    herbs=models.CharField(max_length=100)
    creeper=models.CharField(max_length=100)
    climber=models.CharField(max_length=100)
    def __str__(self):
        return self.tree

class oder_item(models.Model):
    inside_order=models.ForeignKey(Order,on_delete=models.CASCADE)
    number_of_seedings=models.IntegerField()