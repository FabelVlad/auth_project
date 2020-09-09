from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.base import View, TemplateView

from apps.profiles.models import Profile


class HomePage(TemplateView):
    template_name = 'home.html'


class ProfileView(DetailView):
    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
