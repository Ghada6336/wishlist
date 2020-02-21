from django.contrib import admin

from .models import Item
from .models import NewItem

admin.site.register(Item)
admin.site.register(NewItem)
