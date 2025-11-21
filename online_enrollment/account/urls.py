from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('enrollment/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollment/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    path('subject/add/', views.subject_add, name='subject_add'),
    path('subject/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
]
