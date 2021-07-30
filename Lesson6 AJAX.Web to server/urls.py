from django.conf.urls import url,include
from django.contrib import admin
from test_ajax.views import web,Ajax_func

urlpatterns = [
    url(r'^$',web,name='web'),
    url(r'^ajax_test/',Ajax_func,name='ajax_func'),
]