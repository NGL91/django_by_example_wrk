from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','publish','created',
				  'updated','status')

	list_filter = ('status','created','publish', 'author')

	search_fields = ['title','author__username','publish','status']

	#Auto assign data in slug when input in title in admin interface
	prepopulated_fields = {'slug': ('title',)}

	#Show id of fields instead of list chooser
	raw_id_fields = ('author',)

	date_hierarchy = 'publish'

	ordering = ['status','publish']



#Another way to register admin with Post
# admin.site.register(models.Post, PostAdmin)