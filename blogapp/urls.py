from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name='blog'),
    path('post/<slug:url>', views.post_detail, name='postdetail'),
    path('search', views.search, name='search'),
]