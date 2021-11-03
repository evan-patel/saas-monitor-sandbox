from django.contrib.auth.models import AbstractUser
from django.db import models

from SAAS_MONITOR.models import AbstractIdCreatedUpdatedModel


class User(AbstractIdCreatedUpdatedModel, AbstractUser):
    display_name = models.CharField(max_length=255,
                                    default=None,
                                    blank=True
                                    )
    
    def save(self, *args, **kwargs):
        self.display_name = f"{self.first_name} {self.last_name}"
        super(User, self).save(*args,**kwargs)
