from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from .models import CustomUser, Profile
from django.utils import timezone

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):

    username = credentials.get('username')
    try:
        user = CustomUser.objects.get(username=username)

        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user, first_name=user.first_name,
                                   last_name=user.last_name, email=user.email)
        user.profile.last_failed_login = timezone.now()
        user.profile.save()
    except CustomUser.DoesNotExist:
        pass