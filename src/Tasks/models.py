from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    deadline = models.DateTimeField()
    user = models.IntegerField(db_index=True)

    def __str__(self):
        return self.title
