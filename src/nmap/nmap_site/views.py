from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def site_index(request: HttpRequest):
    return render(request, "nmap_site/site_index.html")

def site_history(request: HttpResponse):
    return render(request, "nmap_site/site_history.html")

def site_description(request: HttpResponse):
    return render(request, "nmap_site/site_description.html")

def site_tech_details(request: HttpResponse):
    return render(request, "nmap_site/site_details.html")

def site_tests(request: HttpResponse):
    return render(request, "nmap_site/site_tests.html")

def site_results(request: HttpResponse):
    return render(request, "nmap_site/site_results.html")

def site_other_tools(request: HttpRequest):
    return render(request, "nmap_site/site_othertools.html")

def site_orchestration(request: HttpResponse):
    return render(request, "nmap_site/site_orchestration.html")