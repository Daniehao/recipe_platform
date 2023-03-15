from django.urls import reverse
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.files.uploadedfile import SimpleUploadedFile
from recipe_platform.settings import MEDIA_ROOT
import tempfile

old_media_path = MEDIA_ROOT
temp_media_path = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=temp_media_path)
class RecipeViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        # Create 3 recipes for pagination tests
        image_path = old_media_path + '/taco.jpeg'
        Recipe.objects.create(title='Easy Taco', creator=test_user1, post_date='2019-09-25 06:00', dish_type='Mexican',
                              difficulty='Easy',
                              photo_1=SimpleUploadedFile(name='taco.jpeg', content=open(image_path, 'rb').read(),
                                                         content_type='image/jpeg'), recipe_content='example steps.')
        image_path = old_media_path + '/steak.jpeg'
        Recipe.objects.create(title='Easy Steak', creator=test_user1, post_date='2019-09-25 06:00',
                              dish_type='American',
                              difficulty='Easy',
                              photo_1=SimpleUploadedFile(name='steak.jpeg', content=open(image_path, 'rb').read(),
                                                         content_type='image/jpeg'), recipe_content='example steps.')
        image_path = old_media_path + '/tiramisu.jpeg'
        Recipe.objects.create(title='Easy Tiramusu', creator=test_user2, post_date='2019-09-25 06:00',
                              dish_type='American',
                              difficulty='Easy',
                              photo_1=SimpleUploadedFile(name='tirmaisu.jpeg', content=open(image_path, 'rb').read(),
                                                         content_type='image/jpeg'), recipe_content='example steps')

    def test_index(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/index.html')
        self.assertTemplateUsed(response, 'recipes/base.html')

    def test_recipe_counts_user_counts(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertTrue('recipes_count' in response.context)
        self.assertEqual(response.context['recipes_count'], 3)
        self.assertEqual(response.context['users_count'], 2)

    def test_get_my_recipes(self):
        response = self.client.get(reverse('recipes:my_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/my_recipes.html')
        self.assertTemplateUsed(response, 'recipes/base.html')

    def test_post_invalid_my_recipes(self):
        image_path = old_media_path + '/orange_chicken.jpeg'
        response = self.client.post(reverse('recipes:my_recipes'), {
            'creator': 'testuser1',
            'title': 'orange chicken',
            'post_date': '2023-01-30 06:00',
            'dish_type': 'Chinese',
            'difficulty': 'Hard',
            # the picture's type is invalid
            'photo_1': SimpleUploadedFile(name='orange_chicken.jpeg', content=open(image_path, 'rb').read(),
                                          content_type='image/png')
        })
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_my_recipes_2(self):
        response = self.client.post(reverse('recipes:my_recipes'), data={})
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        response = self.client.get(reverse('recipes:not_found'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_not_found.html')
        self.assertTemplateUsed(response, 'recipes/base.html')

    def test_recipe_page(self):
        response = self.client.get(reverse('recipes:recipe_page', kwargs={'recipe_id': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_page.html')
        self.assertTemplateUsed(response, 'recipes/base.html')

    def test_get_edit_recipe(self):
        response = self.client.get(reverse('recipes:edit_recipe', kwargs={'recipe_id': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/edit_recipe.html')
        self.assertTemplateUsed(response, 'recipes/base.html')

    def test_delete_recipe(self):
        response = self.client.get('/delete_recipe/2/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/my_recipes/')

    def test_search_found(self):
        response = self.client.get('/search/?recipe_search=taco')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/recipe_page/1/')

    def test_search_not_found(self):
        response = self.client.get('/search/?recipe_search=cake')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/not_found/')
