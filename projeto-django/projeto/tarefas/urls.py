from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('',views.tarefas_home, name='home'),
    path('adicionar/', views.adicionar_tarefas, name='adicionar'),
    path('editar/<int:id>',views.editar_tarefas, name='editar'),
    path('remover/<int:id>', views.tarefas_remover, name='remover')
]