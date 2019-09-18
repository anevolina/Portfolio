from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    source_url = models.CharField(max_length=300)
    image = models.FilePathField(path='anevolina/static/img/')

    def __str__(self):
        return self.title
