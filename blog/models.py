from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	tag = models.TextField()
	lyrics = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	
	def get_tag(self):
		return self.tag

	def get_lyrics(self):
		return self.lyrics


