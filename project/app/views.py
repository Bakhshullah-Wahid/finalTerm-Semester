from django.shortcuts import render , redirect , get_object_or_404

from app.form import FormView, FormViewAut, FormViewAuthor, FormViewLog
from app.models import BlogPost, UserAuthentication

# Create your views here.
def published_blog(request):
    context = BlogPost.objects.all()
    return render(request , 'published_blog.html' , {'blogs':context})

# detailed page for every blog
def published_blog_detail(request , id):
    data =BlogPost.objects.get(pk = id)
    return render(request , 'published_blog_detail.html' , {'blogs':data})


#detail individual blog of an author missing
def author_all_blog(request , authorname):
    context = BlogPost.objects.filter(author__name = authorname)
    data ={'allBlogs':context}
    print(data)
    return render(request , 'author_all_blog.html' ,{'allBlogs':context})


def form_blog_post(request):
    context ={}
    data = FormView(request.POST or None)
    if data.is_valid():
        data.save()
        return redirect('/')
    context['form'] = data
    return render(request , 'for_blog_post.html' , context)

def form_for_author(request):
    context ={}
    data = FormViewAuthor(request.POST or None)
    if data.is_valid():
        data.save()
        return redirect('/')
    context['form'] = data
    return render(request , 'for_blog_post.html' , context)

def delete(request , id):
    dele = BlogPost.objects.get(pk=id)
    dele.delete()
    return redirect('/')

def update(request, id):
    context = {}
    obj = get_object_or_404(BlogPost , pk = id)
    data = FormView(request.POST or None , instance=obj)
    if data.is_valid():
        data.save()
        return redirect('/')
    context['form'] = data
    return render(request , 'update.html' , context)

def authentication(request):
    context = {}
    data = FormViewAut(request.POST or None)
    if data.is_valid():
        data.save()
        return redirect('/')
    context['form'] = data
    return render(request , 'athenticate.html' , context)

def login(request):
    context = {}
    deepdata = UserAuthentication.objects.all()
    data = FormViewLog(request.POST or None)
    if data.is_valid():
        return redirect('/')
    context['form'] = data
    return render(request , 'loginpage.html',context)