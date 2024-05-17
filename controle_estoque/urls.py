
from django.contrib import admin
from django.urls import path
from app_controle_estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota, view responsável, nome de referência
    # controle.com
    path('', views.home, name='home'),
    # controle.com/itens
    path('itens', views.itens, name='listagem_itens'),
]
