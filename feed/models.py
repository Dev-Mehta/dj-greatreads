from urllib.parse import urlparse

from django.db import models


class Submission(models.Model):
    link = models.URLField()

    def __str__(self) -> str:
        return self.link


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    link = models.URLField()
    pub_at = models.DateField()

    def __str__(self) -> str:
        return f"{self.netloc} - {self.title}"

    @property
    def netloc(self) -> str:
        domain = urlparse(self.link).netloc
        return domain
