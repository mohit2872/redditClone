from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models

@login_required
def create(request):
    if request.method == "POST":
        if request.POST["title"] and request.POST["url"]:
            post = models.Post()
            post.title = request.POST["title"]
            if request.POST["url"].startswith("http://") or request.POST["url"].startswith("https://"):
                post.url = request.POST["url"]
            else:
                post.url = "https://" + request.POST["url"]
            post.author = request.user
            post.pub_date = timezone.datetime.now()
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'Please enter both the title and url'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    posts = models.Post.objects.order_by('votes_total')
    return render(request, 'posts/home.html', {'posts': posts})

def upvote(request, pk):
    post = models.Post.objects.get(pk=pk)
    post.votes_total += 1
    post.save()
    return redirect('home')

def downvote(request, pk):
    post = models.Post.objects.get(pk=pk)
    post.votes_total -= 1
    post.save()
    return redirect('home')
