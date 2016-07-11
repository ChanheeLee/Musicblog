from django.shortcuts import render
from django.utils import timezone
from .models import Post,Word
# Create your views here.


def index_page(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	post1 = posts[0]


	words = Word.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


	return render(request,'blog/index.html',{'posts':posts, 'post1':post1, 'words':words})


def list_page(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request,'blog/list.html',{'posts':posts})



