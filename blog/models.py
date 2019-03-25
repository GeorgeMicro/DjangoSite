from django.db import models

# Create your models here.
class Post(models.Model):
	subject = models.CharField(max_length=100)
	# content field will need further revision
	content = models.TextField()
	pub_date = models.DateTimeField()
	label = models.SlugField()
	
	def __str__(self):
		return self.subject
	def get_label(self):
		return self.label