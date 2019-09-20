from django.db import models
from portfolio import settings

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    source_url = models.CharField(max_length=300)
    image = models.FilePathField(path=settings.STATICFILES_DIRS[0] + '/img/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image = self.image.replace(settings.STATICFILES_DIRS[0], '')

        super().save(*args, **kwargs)

