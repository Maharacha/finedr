from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils.translation import pgettext_lazy, gettext_lazy as _
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Automatically create tokens when users are created.
    """
    if created:
        Token.objects.create(user=instance)
    else:
        print("No Token created!")


class ParkingLot(models.Model):
    street_name = models.CharField(
        max_length=100,
        unique=True,
        primary_key=True
    )
    coordinates = models.CharField(
        max_length=200,
        unique=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.street_name


class FineTip(models.Model):
    class Meta:
        verbose_name = pgettext_lazy('singular', 'fine tip')
        verbose_name_plural = pgettext_lazy('plural', 'fine tips')
        ordering = ('-pub_date', )
        
    image = models.ImageField(
        verbose_name=_("preview image"),
        upload_to='%Y/%m/%d/',
        unique=True,
        null=True
    )
    license_plate = models.CharField(
        verbose_name=_("license plate"),
        max_length=6
        )
    reason = models.CharField(
        max_length=100,
        null=True
    )

    parking_lot = models.ForeignKey(
        ParkingLot, verbose_name=_("parking lot"), on_delete=models.PROTECT
    )
        
    coordinates = models.CharField(
        max_length=200,
        null=True
    )
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_by = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(
        verbose_name=_("date found"),
        default=timezone.now
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.license_plate
