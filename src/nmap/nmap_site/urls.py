from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_index, name='site_index'),
    path('history', views.site_history, name='site_history'),
    path('details', views.site_tech_details, name='site_details'),
    path('tests', views.site_tests, name='site_tests'),
    path('results', views.site_results, name='site_results'),
    path('others', views.site_other_tools, name='site_othertools'),
    path('orchestration', views.site_orchestration, name='site_orcherstration'),
]


"""
urls hrefs: 
<baseurl> - home.html
<baseurl>/nmap - site_index.html
<baseurl>/nmap/history - site_history.html
<baseurl>/nmap/details - site_details.html
<baseurl>/nmap/tests - site_tests.html
<baseurl>/nmap/results - site_results.html
<baseurl>/nmap/others - site_othertools.html
<baseurl>/nmap/orchestration - site_orchestration.html
"""

