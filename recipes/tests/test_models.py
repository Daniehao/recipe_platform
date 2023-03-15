from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from recipes.models import Recipe
from recipe_platform.settings import MEDIA_ROOT


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        image_path = MEDIA_ROOT + '/taco.jpeg'
        Recipe.objects.create(title='Easy Steak', creator='Danie', post_date='2019-09-25 06:00', dish_type='Chinese',
                              difficulty='Easy',
                              photo_1=SimpleUploadedFile(name='taco.jpeg', content=open(image_path, 'rb').read(),
                                                         content_type='image/jpeg'))

    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_creator_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('creator').verbose_name
        self.assertEqual(field_label, 'creator')

    def test_post_date_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_dish_type_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('dish_type').verbose_name
        self.assertEqual(field_label, 'dish type')

    def test_difficulty_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('difficulty').verbose_name
        self.assertEqual(field_label, 'difficulty')

    def test_photo_1_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('photo_1').verbose_name
        self.assertEqual(field_label, 'photo 1')

    def test_str(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, recipe.__str__())
