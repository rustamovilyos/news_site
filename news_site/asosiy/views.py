from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Article
from django.core.paginator import Paginator



def index(request):
    maqolalar = Article.objects.all()
    kategoriyalar = Category.objects.all()
    return render(request, 'asosiy/index.html', {'turi': kategoriyalar, 'maqolalar': maqolalar})


def asosiy(request, asosiy_id):
    page = request.GET.get('page')
    kategoriya = Category.objects.get(pk=asosiy_id)
    all_maqolalar = Article.objects.filter(kategoriyasi=kategoriya).order_by(id)
    paginator = Paginator(all_maqolalar, 3)
    maqolalar = paginator.get_page(page)
    kategoriyalar = Category.objects.all()
    return render(request, 'asosiy/index.html', {'turi': kategoriyalar, 'maqolalar': maqolalar})