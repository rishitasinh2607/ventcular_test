from django.db import models

# Create your models
class Users(models.Model):
    customer_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)

      

    
    def __str__(self):
        return f"{self.customer_id} - {self.name}"