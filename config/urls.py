from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.profiles.views import HomePage
from config import settings

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('profile/', include('apps.profiles.urls')),
    path('accounts/', include('allauth.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
