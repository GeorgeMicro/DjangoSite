from django.db import models

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.subject
    
