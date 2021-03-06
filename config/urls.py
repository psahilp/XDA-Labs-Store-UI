"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from previewer.views import MockDataTemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('previewer.urls')),
    url('^store/app/(?P<package_name>.+)$', MockDataTemplateView.as_view(template_name='details.html')),
    url('', MockDataTemplateView.as_view(template_name="index.html")),
    url('^store/author/(?P<username>.+)$', MockDataTemplateView.as_view(template_name='dev.html')),
    url('^store/author/(?P<userid>.+)$', MockDataTemplateView.as_view(template_name='dev.html')),

]
