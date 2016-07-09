from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.


def index_page(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request,'blog/index.html',{'posts':posts})
