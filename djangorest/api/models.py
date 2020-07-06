from django.db import models


class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"