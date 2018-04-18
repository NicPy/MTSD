from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutInfo, News


def index(request):
	news = News.objects.order_by('pub_date')[:3]
	context ={
	'about_text' : AboutInfo.objects.order_by('pub_date')[:1],
	'news': news,

	}
	return render(request, 'homepage.html', context )

def about(request):

	context ={
	'about_text' : AboutInfo.objects.order_by('pub_date')[:1],
	
	}
	return render(request, 'about.html', context)

def news(request):
	news = News.objects.order_by('pub_date')[:20]
	context = {
	'news': news,
	}
	return render(request, 'news.html', context)

def single_news(request, pk):
	news = News.objects.get(pk=pk)

	context ={
		'news': news,
	}
	return render(request, 'single_news.html',context )
