from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('register/', views.registerUser, name="user_register"),
    path('student/', include('student.urls')),
    path('', views.home, name="home"),
    path('token', views.token_send, name='token_send'),
    path('success', views.success, name='success'),
]
