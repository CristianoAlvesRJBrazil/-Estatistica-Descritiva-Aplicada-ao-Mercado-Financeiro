from django.urls import path
from . import views


urlpatterns = [

    path('formulario/', views.buscador_acoes ),
    #path('estatistica/', views.tabela_acoes ),
    #path('formulario/grafico/', views.grafico_barras ),
    
]


