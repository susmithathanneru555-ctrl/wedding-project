from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('next_page.html', views.next_page_view, name='next_page'),
    path('bride.html', views.bride_view, name='bride'),
    path('groom.html', views.groom_view, name='groom'),
]

