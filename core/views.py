from django.shortcuts import render
from blog.models import Post
# Create your views here.

# function based views
# the views are functions where we define what will happen when a user makes a particular request
def frontpage(request):
        post = Post.objects.all()
        return render(request, 'core/frontpage.html', {'post': post})

def about(request):
    return render(request, 'core/about.html')

def contact_us(request):
    return render(request, 'core/contact.html')