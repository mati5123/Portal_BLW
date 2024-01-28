from django.db import models

class Week(models.Model):
    week_number = models.IntegerField()

    def __str__(self):
        return f"Tydzień {self.week_number}"