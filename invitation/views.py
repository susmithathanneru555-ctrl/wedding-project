from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invitation.urls')),  
    path('bride.html',views.bride_view,name='bride'),
    path('groom.html',views.groom_view,name='groom'),
]
