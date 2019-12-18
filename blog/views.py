from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# #list
# posts = [
#     {
#         'author': 'CoreyMS-new',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]

# Create your views here.
def home(request):
    #context 字典
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>My Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})