from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('logout/', views.logoutUser, name = "logout"),
    path('login/', views.loginPage, name ="login"),
    path('register/', views.register, name ="register"),
    path('myimages/', views.myimages, name ="myimages"),
    path('word_prompt/', views.word_prompt, name ="word_prompt"),
]
