from django.contrib import admin
from django.urls import path,include
from .views import Index,signup,Login

urlpatterns = [
    
    path('',Index.as_view(),name='homepage'),
    path('signup/',signup,name='signup'),
    path('login/',Login.as_view(),name='login'),
]