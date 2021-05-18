from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post

def index(request):
	posts = Post.objects.all()
	myname = "童沛瀠"
	data = [ i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	return render(request, 'index.html', locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		target = None
	return render(request, "showpost.html", locals())