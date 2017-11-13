#coding:utf8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
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
	body = UEditorField(u"文章正文",height=300,width=700,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')
	created_time = models.DateTimeField(u"发布日期",default = timezone.now,editable=True)
	modified_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
	excerpt = models.CharField(verbose_name='摘要',max_length=200,blank=True)
	category = models.ForeignKey(Category,verbose_name='分类')
	tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
	author = models.ForeignKey(User,verbose_name='用户')
	views = models.PositiveIntegerField(default=0)

	def increase_views(self):
		self.views +=1
		self.save(update_fields=['views'])
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-created_time']