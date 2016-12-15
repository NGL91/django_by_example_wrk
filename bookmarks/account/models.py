from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)


from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kw):
	if created:
		profile =Profile(user=instance)
		profile.save()