from django.db import models
from django.contrib.auth.models import User

class Graduator(object):
    name = models.CharField(max_length=50)        
    surname = models.CharField(max_length=50)        
    patronymic = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    work_place = models.CharField(max_length=250)
    help_with = models.CharField(max_length=500)
    help_with = models.CharField(max_length=500)
    need_help_with = models.CharField(max_length=500)
    email = models.EmailField(max_length=240)


class NewsCategory(models.Model):
    cat_name = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.cat_name


class News(models.Model):
    item_title = models.CharField(max_length=110) 
    item_text = models.TextField(max_length=3000)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField(default = True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_title

class Project(models.Model):
    item_title = models.CharField(max_length=110)
    item_text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.item_title

        
class StaticPage(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    item_title = models.CharField(max_length=110)
    item_text = models.TextField(max_length=3000)
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.item_title