from django.urls import path

from apps.profiles.views import ProfileView, HomePage

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
]
