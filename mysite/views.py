from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import random
from mysite.models import Post, Country, City

def index(request):
	posts = Post.objects.all()
	myname = "童沛瀠"
	data = [i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	return render(request, 'index.html', locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

def logout(request):
	auth.logout(request)
	return redirect("/")

def rank(request):
	cities = City.objects.all()
	return render(request, "rank.html", locals())


