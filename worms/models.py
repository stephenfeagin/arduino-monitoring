from django.db import models


class Measurement(models.Model):
    insert_timestamp = models.DateTimeField(auto_now=True)
    humidity = models.IntegerField()
    temperature = models.IntegerField()

    class Meta:
        ordering = ["insert_timestamp"]

    def __str__(self):
        return f"Measurement {self.insert_timestamp}"
