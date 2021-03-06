# monitor/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


# router = routers.DefaultRouter()


urlpatterns = [
    # path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("worms/", include("worms.urls")),
]
