from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^home/$', views.home, name='home'),
    path('addgroup/', views.addgroup, name='addgroup'),
    path('viewgroups/', views.viewgroups, name='viewgroups'),
    path('viewhistory/', views.viewhistory, name='viewhistory'),
    path('addtransaction/', views.addtransaction, name='addtransaction'),
    path('settleup/', views.settleup, name='settleup'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]