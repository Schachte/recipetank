from django.db import models

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	instructions = models.TextField()
	tag = models.CharField(max_length=20, blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name