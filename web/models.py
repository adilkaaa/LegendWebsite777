from django.db import models


# Create your models here.


class Portfolio(models.Model):
    image = models.ImageField(upload_to='files/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk


class Blog(models.Model):
    image = models.ImageField(upload_to='files/%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk


class Employer(models.Model):
    image = models.ImageField(upload_to='files/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class SendToEmail(models.Model):
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.mail


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length=40, blank=True)
    message = models.TextField(blank= True)

    def __str__(self):
        return self.name
