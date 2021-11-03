import uuid

from django.db import models


class AbstractIdCreatedUpdatedModel(models.Model):
    '''
    This is a abstract model which creates
    ID ----> UUID
    CREATED AT -----> DATE AND TIME
    UPDATED AT -----> DATE AND TIME
    '''
    id = models.UUIDField(uuid.uuid4,
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False,
                                      )
    updated_at = models.DateTimeField(auto_now=True,
                                      editable=False
                                      )

    class Meta:
        abstract = True
