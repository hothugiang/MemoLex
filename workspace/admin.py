from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Package)
admin.site.register(models.User_Package)
admin.site.register(models.Word_Package)