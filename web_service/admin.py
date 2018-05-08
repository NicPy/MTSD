from django.contrib import admin

from .models import News, NewsCategory, Project, StaticPage

admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Project)
admin.site.register(StaticPage)