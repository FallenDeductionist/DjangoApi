from django.db import models

# Create your models here.


class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    image = models.FileField(upload_to='storage/images/', max_length=250, null=True)
    navigation = models.CharField(max_length=100)

    def __str__(self):
        return self.title
