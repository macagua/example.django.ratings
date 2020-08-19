from django.db import models
from django.utils.translation import gettext_lazy as _

class Destinations(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=200,
        blank=True,
        null=True,
    )

    short_description = models.TextField(
        _('Short description'),
        blank=True,
        null=True,
    )

    description = models.TextField(
        _('Description'),
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _('Destinations')
