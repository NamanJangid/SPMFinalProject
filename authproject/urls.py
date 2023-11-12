from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.login_request),
   path('main/',views.main_request),
   path('main/repos/',views.repos)

]