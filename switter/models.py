from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False, # users can follow someone without them following back
        blank=True
    )

    def __str__(self):
        return self.user.username


# ------------------------------
#            SIGNALS
# ------------------------------
def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # newly created user automatically follows their own profile
        user_profile.follows.add(instance.profile)
        user_profile.save()

# Create a Profile for each new user
post_save.connect(create_profile, sender=User)