from django.db import models

# Create your models here.

class findUser(models.Model):
    name=models.CharField(max_length=30)
    whatsapp_number=models.CharField(max_length=10)
    instagram_username=models.CharField(max_length=200)
    discord_username=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

