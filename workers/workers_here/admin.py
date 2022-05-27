from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Workers

# Register your models here.

admin.site.register(Workers, MPTTModelAdmin)