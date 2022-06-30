from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from users.urls import user_routes

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(user_routes.urls))
]
