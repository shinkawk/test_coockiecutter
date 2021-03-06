"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path(
        "api/",
        include(
            [
                path("", include("authentication.api_urls")),
            ]
        ),
    ),
]

if settings.DEBUG:
    SchemaView = get_schema_view(
        openapi.Info(
            title="Server API",
            default_version="v1",
            description="API Listg",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [re_path(r"^swagger/$", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui")]

    # /staticも入れておく
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if settings.MEDIA_URL != "/":
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
