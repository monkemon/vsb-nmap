from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def site_index(request: HttpRequest):
    return HttpResponse('nmap_site/site_index.html')

def site_history(request: HttpResponse):
    return HttpResponse('nmap history')

def site_description(request: HttpResponse):
    return HttpResponse('nmap description')

def site_tech_details(request: HttpResponse):
    return HttpResponse('details')

def site_tests(request: HttpResponse):
    return HttpResponse('tests explaination')

def site_results(request: HttpResponse):
    return HttpResponse('test results')

def site_other_tools(request: HttpRequest):
    return HttpResponse('other tools')

def site_orchestration(request: HttpResponse):
    return HttpResponse('orchestration')