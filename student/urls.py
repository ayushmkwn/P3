from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home_Page.as_view(),name="home_page"),
    path('create/',views.StudentCreate.as_view(),name="create_page"),
    path('<int:pk>/',views.StudentDetails.as_view(),name="details_page"),
    path('<int:pk>/update',views.StudentUpdate.as_view(),name="update_page"),
    path('<int:pk>/delete',views.StudentDelete.as_view(),name="delete_page"),
]
