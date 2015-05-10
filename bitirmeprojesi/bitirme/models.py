from django.db import models

# Create your models here.

class Kampanya(models.Model):
    olusturulma = models.DateTimeField(auto_now_add=True)
    baslik = models.CharField(max_length=100, blank=True, default='')
    icerik = models.TextField()
    onay = models.BooleanField(default=False)

    class Meta:
        ordering=('olusturulma',)
