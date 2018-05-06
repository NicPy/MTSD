from django.db import models
from django.contrib.auth.models import User


class NewsCategory(models.Model):
    cat_name = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

class News(models.Model):
    item_title = models.CharField(max_length=110) 
    item_text = models.TextField(max_length=3000)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField(default = True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)


class AboutInfo(models.Model):
    item_title = models.CharField(max_length=110)
    item_text = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')

class Project(models.Model):
    item_title = models.CharField(max_length=110)
    item_text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

class StaticPage(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    item_title = models.CharField(max_length=110)
    item_text = models.TextField(max_length=3000)
