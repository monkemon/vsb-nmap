from django.shortcuts import render

def home(request):
    template = "home/home.html"
    context = {}
    return render(request, template, context)
