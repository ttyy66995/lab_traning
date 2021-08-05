from django.conf.urls import url,include
from django.contrib import admin
#from . import views
from stock_search.views import web,Ajax_func

urlpatterns = [
    url(r'^$',web,name='web'),
    url(r'^ajax_stock/',Ajax_func,name='ajax_func'),
] 