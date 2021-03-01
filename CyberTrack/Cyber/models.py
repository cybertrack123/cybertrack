from django.db import models

# Create your models here.
class Username(models.Model):
    User = models.CharField(max_length= 50)
    Email = models.CharField(max_length= 50)
    Pass = models.CharField(max_length= 50)

    def __str__(self):
        return self.User

class Commment(models.Model):
    Comment_Text = models.CharField(max_length= 50)