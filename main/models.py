from django.db import models

class InputList(models.Model):
    data = models.JSONField()
