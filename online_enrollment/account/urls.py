from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),      
    path('logout/', views.logout_view, name='logout'), 
    path('enrollment/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollment/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
]
