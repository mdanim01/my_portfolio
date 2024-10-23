from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def services(request):
    return render(request,'services/services.html')
def blog(request):
    return render(request,'blog/blog.html')
def portfolio(request):
    return render(request,'portfolio/portfolio.html')
def contact(request):
    return render(request,'contact/contact.html')