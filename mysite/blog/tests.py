from django.test import TestCase
from . import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your tests here.
class TestBlogPost(TestCase):
	def setUp(self):
		User = get_user_model()
		self.author = User.objects.create(username='luanng',
										  password='213')
		self.author.save()


	def testPostCreation(self):
		post = models.Post(title='First Blog Post',
						   author=self.author,
						   body="This is the body of blog post"
			)


		# self.assertTrue(post.publish==post.created)
		self.assertTrue(post.created==post.updated)
		self.assertTrue(post.status=='draft')

		post.updated = timezone.now()
		self.assertTrue(post.updated!=post.created)

		publish_time = timezone.now()

		post.slug="Slug data for post"
		post.publish = publish_time
		post.save()

		post1 = models.Post(title='Second Blog Post',
						   author=self.author,
						   body="This is the body of blog post"
			)

		#Its only affect from front end
		with self.assertRaises(ValidationError, 
							msg="SlugField didn't raise ValidationError"):
			post1.slug = "Slug data for post"
			post1.publish = publish_time
			post1.save()




	def tearDown(self):
		self.author.delete()