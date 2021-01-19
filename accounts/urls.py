from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name="profile_edit"),
    path('password_change/', views.password_change, name='password_change'),
]