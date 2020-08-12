from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
	title = models.CharField(verbose_name= 'Заголовок', max_length=80, default=None)
	content = models.CharField(verbose_name = 'Содержание', max_length=1000, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='posts_images/')

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		
	def __str__(self):
		return "%s" % self.title