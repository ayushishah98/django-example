from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('registration/', views.registration,name='registration'),
    path('user_login/', views.user_login,name='user_login'),
]
