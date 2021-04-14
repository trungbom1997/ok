from django.db import models

class Customer(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.TextField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user
