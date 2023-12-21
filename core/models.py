from django.db import models
import json


class JsonFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    json_file = models.FileField(upload_to='json_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.json_file}'
