from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gare_list/', views.gare_list, name='gare_list'),
    path('simple_search/', views.simple_search, name='simple_search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)