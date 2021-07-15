from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length=200)
    address= models.TextField()

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:50]
