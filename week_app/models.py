from django.db import models
from django.utils import timezone

# Create your models here.
class Died(models.Model):

    name = models.CharField(max_length=64)
    text = models.TextField()
    edit = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Died: [{self.id}] {self.name}"

