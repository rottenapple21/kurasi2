from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Input(models.Model):
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # 
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    nama = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_posted = models.DateTimeField(default=timezone.now)
    judul = models.CharField(max_length=100)
    kategori = models.CharField(max_length=100)
    link = models.TextField()
    kelas = models.CharField(max_length=100)
    pelajaran = models.CharField(max_length=100)

    def __str__(self):
        return self.judul
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
