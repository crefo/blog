# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categories(models.Model):
	title=models.CharField(max_length =40, null=False)

	def __str__ (self):
		return self.title
		
class TagModel(models.Model):
	title=models.CharField(max_length =20, null=False)

	def __str__ (self):
		return self.title

class Entries(models.Model):
	title = models.CharField(max_length =80, null=False)
	content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Categories)
	tags = models.ManyToManyField(TagModel)
	comments = models.PositiveSmallIntegerField(default=0, null=True)
	pop = models.PositiveIntegerField(default=0, null=False)
	readed = models.PositiveIntegerField(default=0, null=False)
	
class CommentsModel(models.Model):
	name= models.CharField(max_length =20, null=False)
	pwd = models.CharField(max_length =32, null=False)
	content = models.TextField(max_length =2000, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=True)
	entry = models.ForeignKey(Entries)

	def __str__ (self):
		return "%s // %s // %s // %s" % (self.name, self.pwd, self.content, self.created)

class TimeTest(models.Model):
	test1 = models.DateTimeField()
	test2 = models.DateTimeField("test When Created", auto_now_add=True)
	test2.editable = True
	test3 = models.DateTimeField(auto_now=True)
	test3.editable = True
