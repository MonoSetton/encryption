from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('playfair_encryption', views.playfair_encryption, name='playfair_encryption'),
    path('playfair_decryption', views.playfair_decryption, name='playfair_decryption'),
]