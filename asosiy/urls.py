from django.urls import path
from asosiy import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import ArticleView

app_name='asosiy'
urlpatterns = [
    path('', views.index, name='index'),
    path('asosiy/<int:asosiy_id>/', views.asosiy, name='asosiy'),
    path('team/', TemplateView.as_view(template_name='asosiy/team_info.html'), name='team'),
    path('maqola/<int:pk>/', ArticleView.as_view(), name='batafsil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
