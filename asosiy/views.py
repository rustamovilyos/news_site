from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Article
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

app_name='asosiy'


def index(request):
    maqolalar = Article.objects.all()[:3]
    kategoriyalar = Category.objects.all()
    return render(request, 'asosiy/index.html', {'turi': kategoriyalar, 'maqolalar': maqolalar})


def asosiy(request, asosiy_id):
    page = request.GET.get('page')
    tip = Category.objects.get(pk=asosiy_id)
    kategoriyalar = Category.objects.all()
    all_maqolalar = Article.objects.filter(toifa=tip)
    paginator = Paginator(all_maqolalar, 2)
    maqolalar = paginator.get_page(page)

    return render(request, 'asosiy/index.html', {'turi': kategoriyalar, 'maqolalar': maqolalar})


class ArticleView(DetailView):
    model = Article
    template_name = 'asosiy/articleView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['turi'] = Category.objects.all()
        return context