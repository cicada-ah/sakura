from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(verbose_name='标题',max_length=70)
	body = models.TextField(verbose_name='内容',)
	created_time = models.DateTimeField(verbose_name='创建时间',)
	modified_time = models.DateTimeField(verbose_name='修改时间',)
	excerpt = models.CharField(verbose_name='摘要',max_length=200,blank=True)
	category = models.ForeignKey(Category,verbose_name='分类')
	tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
	author = models.ForeignKey(User,verbose_name='用户')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-created_time']