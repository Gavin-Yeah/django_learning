from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    categoty_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact timee")

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()
    def __str__(self) -> str:
        return self.first_name
