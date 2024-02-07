from django.urls import path, include

from auth_system_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.home, name='home'),

    path('signup', views.signup_views, name='signup_page'),
    path('login', views.login_views, name='login_page'),
    path('logout', views.logout_views, name='logout_page'),

]