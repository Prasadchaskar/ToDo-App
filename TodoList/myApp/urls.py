from django.urls import path,include
from . views import home,Detail,Create,Update,Delete
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('',home.as_view(),name="home"),
    path('detail/<int:pk>',Detail.as_view(),name="detail"),
    path('create/',Create.as_view(),name="create"),
    path('update/<int:pk>',Update.as_view(),name="update"),
    path('delete/<int:pk>',Delete.as_view(),name="delete"),
    path('register/',views.register,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login')
]