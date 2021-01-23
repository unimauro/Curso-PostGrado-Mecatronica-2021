from django.db import models

# Create your models here.
class Complemento(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Polleria(models.Model):
    tipo1 = models.CharField(max_length=100)
    tipo2 = models.CharField(max_length=100)
    complemento = models.ForeignKey(Complemento, on_delete=models.CASCADE)

