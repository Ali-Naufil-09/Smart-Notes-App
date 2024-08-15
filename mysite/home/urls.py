from django.urls import path
from .import views



urlpatterns = [
   #method1: path('',views.home),   #this urls.py is a file created by me . it ensures that if home app is deleted than even than everthing will work properly
   #method 2:
   path('',views.HomeView.as_view()),
   #method1:  path('authorized/',views.authorized),
   #path('authorized/',views.AuthorizedView.as_view(), name='home'),
   path('login/' , views.LoginInterfaceView.as_view(),name='login'),
   path('logout/' ,views.LogoutInterfaceView.as_view(),name='logout'),
   path('signup/' ,views.SignupView.as_view(),name='signup'),
]