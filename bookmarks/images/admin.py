from django.contrib import admin
from .models import Image
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['title','slug','image','created']

	list_filter = ['created']
	date_hierarchy = 'created'

	raw_id_fields = ['user']

	prepopulated_fields = {'slug': ('title',)}