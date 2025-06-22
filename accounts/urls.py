from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'),name='logout'),
]
