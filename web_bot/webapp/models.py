from django.db import models

# Create your models here.
class Detail(models.Model):
    Name = models.CharField(max_length=250)
    Brand_name = models.CharField(max_length=250)
    info = models.TextField()
    About = models.TextField()
    quotes = models.TextField()
    logo_image = models.ImageField(upload_to='pics')
    your_upi = models.CharField(max_length=250)
    contact_1 = models.CharField(max_length=250)
    contact_2 = models.CharField(max_length=250)
    whatsapp = models.CharField(max_length=250)
    def __str__(self):
        return self.Name

class Telegram_project(models.Model):
    Telegram_bot = models.CharField(max_length=250)
    Telegram_icon = models.ImageField(upload_to="pics")
    def __str__(self):
        return self.Telegram_bot

class Github_project(models.Model):
    Repository_name = models.CharField(max_length=250)
    def __str__(self):
        return self.Repository_name

class Account(models.Model):
    Github = models.CharField(max_length=250)
    Facebook = models.CharField(max_length=250)
    Telegram = models.CharField(max_length=250)
    Twitter = models.CharField(max_length=250)
    def __str__(self):
        return self.Github

