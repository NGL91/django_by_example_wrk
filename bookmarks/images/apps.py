from django.apps import AppConfig

class ImageConfig(AppConfig):
	name='images'
	verbose_name='Image bookmarks'

	def ready(self):
		#import signal handlers
		import images.signals