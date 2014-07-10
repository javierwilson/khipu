from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from zinnia.models.entry import Entry
from zinnia.admin.entry import EntryAdmin

class EntryKhipuAdmin(EntryAdmin):
  # we put the 'source' field into the 'Content' fieldset
  fieldsets = ((_('Content'), {'fields': (
    ('title', 'status'), 'content', 'image', 'source')}),) + \
    EntryAdmin.fieldsets[1:]

# Unregister the default EntryAdmin
# then register the EntryKhipuAdmin class
admin.site.unregister(Entry)
admin.site.register(Entry, EntryKhipuAdmin)
