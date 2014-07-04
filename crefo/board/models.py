# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
	name = models.CharField(max_length=256)

class Board(models.Model):
	type = models.ForeignKey(Type)
	userID = models.ForeignKey(User)

	writer = models.CharField(max_length=32)
	tilte = models.CharField(max_length=256)
	content = models.TextField()
	like = models.PositiveSmallIntegerField()			# 0 to 32767
	putUpDate = models.DateTimeField(auto_now_add=True)
	finalUpDate = models.DateTimeField(auto_now=True)
	
class Comments(models.Model):
	board = models.ForeignKey(Board)
	userID = models.ForeignKey(User)
	writer = models.CharField(max_length=32)
	upDate = models.DateTimeField(auto_now=True)
	comment = models.CharField(max_length=512)
	