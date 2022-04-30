from django.test import TestCase

from .models import Category

class CategoryTest(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Other',slug='other',details='')
    
    def test__str__(self):
        pass
        # data = self.data1
        # self.assertTrue(isinstance(data, Category))
        # self.assertEqual(str(data), 'Other')
    # def test_category_url(self):
    #     """
    #     Test category model slug and URL reverse
    #     """
    #     data = self.data1
    #     response = self.client.post(
    #         reverse('MVC:category_list', args=[data.slug]))
    #     self.assertEqual(response.status_code, 200)