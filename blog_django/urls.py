from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title="API", default_version='v1'),
                              public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
