from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Died(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    week_number = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='week_app/static/died_images/', blank=True, null=True)


    def __str__(self):
        return f"Died: [{self.id} {self.name} "

class Comment(models.Model):
    died = models.ForeignKey(Died, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



class Image(models.Model):
    died = models.ForeignKey(Died, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='week_app/static/died_images/', blank=True, null=True,)




    def __str__(self):
        return f"Image for Died: {self.died.name}"


