from django.db import models
from zinnia.models_bases.entry import AbstractEntry

class EntryKhipu(AbstractEntry):
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta(AbstractEntry.Meta):
        abstract = True
