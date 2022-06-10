from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=264,unique=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message