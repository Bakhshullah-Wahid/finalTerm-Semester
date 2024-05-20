
from django.urls import path
from django.http import HttpResponse

from app import views


urlpatterns = [
    path('' , views.published_blog , name='publishedBlog') ,
    path('published_blog_detail/<int:id>' , views.published_blog_detail , name='publishedBlogDetail'),
    path('author_all_blog/<str:authorname>' , views.author_all_blog , name='authorAllBlog'),
    path('form_blog_post' , views.form_blog_post , name='formBlogPost'),
    path('form_author',views.form_for_author ,name='form_for_author'),
    path('delete/<int:id>' , views.delete , name ='delete'),
    path('update/<int:id>' , views.update , name='update'),
    path('authentication' , views.authentication , name='authenticate'),
    path('login' , views.login , name='login')
]