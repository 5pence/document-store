from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(MyChunkedUpload)
class MyChunkedUploadAdmin(admin.ModelAdmin):
    pass