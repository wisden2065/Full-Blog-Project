from django.shortcuts import render

# Create your views here.

# function based views
# the views are functions where we define what will happen when a user makes a particular request
def frontpage(request):
        return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')

def contact_us(request):
    return render(request, 'core/contact.html')