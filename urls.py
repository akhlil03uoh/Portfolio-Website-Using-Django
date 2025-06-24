from django.urls import path
from webApp import views
from django.urls import path
from . import views

urlpatterns = [
    path('Base/', views.Base, name='Base'),  # ✅ 'base' name defined here
    # The 'home' name is defined in the Home view below
    # path('Home/', views.Home, name='Home'),  # This line is redundant if the Home view is already defined with the same name
    # If you want to keep it, you can uncomment it, but it's not necessary since 'Home' is already defined below
    path('', views.Home, name='Home'),  # ✅ 'home' name defined here
    path('About/', views.About, name='About'),
    path('Projects/', views.Projects, name='Projects'),
    path('Resume/', views.Resume, name='Resume'),
    path('Contact/', views.Contact, name='Contact'),
]