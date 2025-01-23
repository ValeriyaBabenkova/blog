from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def main (request):
    posts = Post.objects.all()
    return render (request, 'index.html', {'posts': posts})


def post_detail(request, post_id):
     post = Post.objects.get(id=post_id)

     return render (request, 'post_detail.html', {'post':post})

def post_add(request):
    def post_add(request):
        # достать месяц по номеру и отдать описание

        post = Post.objects.get()

        if request.method == 'POST':
            title = request.POST.get('title')
            text = request.POST.get('text')
            post.title = title
            post.text  = text
            post.save()

        return render(request, 'post_add.html', {'post':post})