from django.conf import settings
from django.conf.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path, path
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='main/index.html'), name='home'),
    re_path(r'^api/crawl/', views.crawl, name='crawl'),
    path('api/showdata/', views.show_data, name='show_data')
]

