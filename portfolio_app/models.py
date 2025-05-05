from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Nama kelas icon, misal: ri-computer-line")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactRequest(models.Model):
    # field-field Anda di sini
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)