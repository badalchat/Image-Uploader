from django.contrib import admin
from testApp.models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']

admin.site.register(Image, ImageAdmin)