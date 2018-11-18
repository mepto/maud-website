from django.db import models


class CvLine(models.Model):
    period = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text
