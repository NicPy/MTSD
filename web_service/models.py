from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)
    country     = models.CharField(max_length=50)
    city        = models.CharField(max_length=50)
    work_place  = models.CharField(max_length=250)
    help_with   = models.CharField(max_length=500)
    need_help_with = models.CharField(max_length=500)
    contact_info = models.CharField(max_length=400)
    age = models.IntegerField(default=0)
    photo = models.ImageField(null=True, upload_to='images' )

    # avatar = models.ImageField(upload_to="photos", default=)
    # registration_date = models.DateTimeField('date published')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = "True")
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