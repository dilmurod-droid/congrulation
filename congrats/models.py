from django.db import models

class Congratulation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.name} - {self.created_at}"

class Rasmlar(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/')
