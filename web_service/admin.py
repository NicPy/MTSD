from django.contrib import admin

from .models import News, NewsCategory, Project, StaticPage

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)

admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Project)
admin.site.register(StaticPage)