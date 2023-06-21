from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=64, null=False, blank=True)
    description = models.TextField(default='Description is empty')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name