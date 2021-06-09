from django.db import models


# Category - yangiliklar kategoriyasi(turi)
class Category(models.Model):
    nomi = models.CharField('Kategoriya nomi', max_length=60)


# Article - Maqolalar
class Article(models.Model):
    nomi = models.CharField('Nomi', max_length=80)
    muallif = models.CharField('Muallif:', max_length=50)
    tarif = models.TextField(null=True)
    toifa = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    rasm = models.ImageField(null=True)