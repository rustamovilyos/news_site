from django.test import TestCase
from django.test import Client
from django.urls import reverse
from asosiy.models import Category, Article


class ModelTestCase(TestCase):
    def setUp(self):
        Category.objects.create(nomi='test1')
        Category.objects.create(nomi='test2')
        Category.objects.create(nomi='test43')

        Article.objects.create(
            nomi='maqola1',
            muallif='kimdir',
            tarif='Lorem ipsum dolor sit amet',
            toifa=Category.objects.get(nomi='test1')
        )
        Article.objects.create(
            nomi='maqola2',
            muallif='kimdirlar',
            tarif='Lorem ipsum dolor sit amet',
            toifa=Category.objects.get(nomi='test2')
        )
        Article.objects.create(
            nomi='maqola3',
            muallif='kimlar',
            tarif='Lorem ipsum dolor sit amet, consectetur adipisicing elit',
            toifa=Category.objects.get(nomi='test43')
        )

    def test_model_created(self):
        c1 = Category.objects.get(nomi='test1')
        c2 = Category.objects.get(nomi='test2')
        c3 = Category.objects.get(nomi='test43')
        a1 = Article.objects.get(nomi='maqola1')
        a2 = Article.objects.get(nomi='maqola2')
        a3 = Article.objects.get(nomi='maqola3')
        self.assertEqual(c1.nomi, 'test1')
        self.assertEqual(c2.nomi, 'test2')
        self.assertEqual(c3.nomi, 'test43')
        self.assertEqual(a1.toifa, c1)
        self.assertEqual(a2.toifa, c2)
        self.assertEqual(a3.toifa, c3)


class ViewsTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('asosiy:index'))
        self.assertEqual(response.status_code, 200)

        Category.objects.create(nomi='test1')
        Category.objects.create(nomi='test2')
        Category.objects.create(nomi='test43')

        Article.objects.create(
            nomi='maqola1',
            muallif='kimdir',
            tarif='Lorem ipsum dolor sit amet',
            toifa=Category.objects.get(nomi='test1')
        )
        Article.objects.create(
            nomi='maqola2',
            muallif='kimdirlar',
            tarif='Lorem ipsum dolor sit amet',
            toifa=Category.objects.get(nomi='test2')
        )
        Article.objects.create(
            nomi='maqola3',
            muallif='kimlar',
            tarif='Lorem ipsum dolor sit amet, consectetur adipisicing elit',
            toifa=Category.objects.get(nomi='test43')
        )

        response = self.client.get(reverse('asosiy:index'))
        self.assertEqual(response.status_code, 200)

class UrlTestCase(TestCase):
    def test_batafsil_page(self):
        response = self.client.get(reverse('asosiy:batafsil'))
        self.assertEqual(response.status_code, 200)
