from django.contrib import admin

from .models import News, NewsCategory, AboutInfo, Project, StaticPage

admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(AboutInfo)
admin.site.register(Project)
admin.site.register(StaticPage)