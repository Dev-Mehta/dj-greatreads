from django.db import models


class Submission(models.Model):
    link = models.URLField()

    def __str__(self) -> str:
        return self.link
