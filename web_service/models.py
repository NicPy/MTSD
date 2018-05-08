from django.db import models
from django.contrib.auth.models import User


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