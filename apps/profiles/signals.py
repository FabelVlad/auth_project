from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver

from apps.profiles.models import User, Profile


@receiver(user_signed_up, sender=User)
def create_profile(request, user, **kwargs):
    Profile.objects.create(user=user, image=SocialAccount.objects.get(user=user).extra_data.get('picture'))
