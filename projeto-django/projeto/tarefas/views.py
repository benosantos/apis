from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest


def tarefas_home(request):
    context = {
        'nome': 'Beno',
        'tarefas': TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', context)


def adicionar_tarefas(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')

    context = {
        'form': TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', context)


def editar_tarefas(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    formulario = TarefaForm(instance=tarefa)
    context = {
        'form': formulario
    }
    return render(request, 'tarefas/editar.html', context)



def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect('tarefas:home')
