from django.contrib import admin
from .models import Category, Article



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi',)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'muallif', 'toifa', 'vaqt',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)