from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import News, StaticPage
from .forms import UserCreateForm, Profile


def index(request):
	user = request.user
	news = News.objects.order_by('pub_date')[:3]
	context ={
	'user': user,
	'about_text' : StaticPage.objects.get(slug = 'About'),
	'news': news,

	}
	return render(request, 'homepage.html', context )

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url="/login/")
def profile(request):
	user = request.user
	initial = {
			"country": user.userprofile.country,
			"city": user.userprofile.city,
			}
	if request.method == "POST":
		form = Profile(request.POST, instance = user.userprofile )
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			# form.save()
			return redirect("/profile/")
		else:
			HttpResponse("SMTH IS Wrong")
	else:
		form = Profile(instance = user.userprofile, initial = initial)

	context ={
		"form": form,
		"user": user,
	}
	return render(request, "profile.html", context)


def about(request):

	context ={
	'about_text' : StaticPage.objects.get(slug='About'),
	
	}
	return render(request, 'about.html', context)

def charity(request):
	context = {
		'charity_text' : get_object_or_404(StaticPage, slug = 'Charity')
	}
	return render(request, 'charity.html', context)

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
