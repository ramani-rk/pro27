from django.contrib import admin
from django.http import HttpResponse
from app.models import *

# Register your models here.

admin.site.register (Topics)
admin.site.register (Webpage)
admin.site.register (Accessrecord)
