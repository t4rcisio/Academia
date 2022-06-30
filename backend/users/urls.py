from django.urls import path
from rest_framework.routers import format_suffix_patterns

from .views import RegisterView, LoginView, LogoutView
from .adapters import DefaultRouterWithSimpleViews

user_routes = DefaultRouterWithSimpleViews()
user_routes.register('register', RegisterView, 'Register-user')
user_routes.register('login', LoginView, 'Login')
user_routes.register('logout', LogoutView, 'Logout')
