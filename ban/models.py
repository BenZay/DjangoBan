from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.conf import settings


@python_2_unicode_compatible
class UsersBan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name="User name",
                             help_text="Choose Username")

    ban = models.BooleanField(default=False,
                              verbose_name="Ban",
                              help_text="Users Bans")

    class Meta:
        verbose_name_plural = "Ban Management"
        ordering = ('user',)

    def __str__(self):
        return '{0}'.format(self.user)
