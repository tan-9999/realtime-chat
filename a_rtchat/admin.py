from django.contrib import admin # type: ignore
from .models import *

# Register your models here.
admin.site.register(ChatGroup)
admin.site.register(GroupMessage)