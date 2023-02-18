from django.contrib import admin

# Register your models here.
from . models import team
from.models import place
admin.site.register(place)

admin.site.register(team)