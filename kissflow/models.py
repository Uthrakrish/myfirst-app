from django.db import models


class Kissflow(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __repr__(self):
        return self.tilte
