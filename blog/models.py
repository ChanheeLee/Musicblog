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



class Word(models.Model):
	wirter = models.ForeignKey('auth.User')
	writer_name = models.TextField(max_length=20)
	words = models.TextField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)


