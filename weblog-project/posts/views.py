from typing import Any
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic

from .models import Post,Comment
from .forms import PostForm

def index(request):
    return HttpResponse('<h1>Welcom to Django</h1> ')

def home(request):
    return HttpResponse('<h3>Welcom to My Blog ......</h3> ')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,
                  '/home/dci-student/Desktop/excersises/django-home-project/weblog-project/posts/templates/posts/post_list.html',
                    context=context)

class PostList(generic.ListView ):
    queryset= Post.objects.all()
    template_name = '/home/dci-student/Desktop/excersises/django-home-project/weblog-project/posts/templates/posts/post_list.html'
    context_object_name = 'posts'
     

def post_detail(request, post_id):
    
  #  try:
   #     post = Post.objects.get(pk=post_id) 
    #except Post.DoesNotExist:
     #   return HttpResponseNotFound('Post is not exist')
    post = get_object_or_404(Post,pk= post_id)
    comments = Comment.objects.filter(post = post)
    context = {'post': post,'comments':comments }
    return render(request, 
                  '/home/dci-student/Desktop/excersises/django-home-project/weblog-project/posts/templates/posts/post_detail.html'
                  ,context= context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = '/home/dci-student/Desktop/excersises/django-home-project/weblog-project/posts/templates/posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context= super(PostDetail,self).get_context_data()
        context['comment'] = Comment.objects.filter(post= kwargs['object'].pk)
        return context

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()

    return render(request,'/home/dci-student/Desktop/excersises/django-home-project/weblog-project/posts/templates/posts/post_create.html',{'form':form})


