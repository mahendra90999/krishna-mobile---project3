from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="mobileview"),
    path('vivo/', views.index,name="mobileview"),
    path('about/',views.about,name="about"),
    path('viewcheck/<str:myid>/',views.viewcheck,name="viewcheck"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('checkout/',views.checkout,name="checkout"),
]