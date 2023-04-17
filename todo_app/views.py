from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ToDoForm
from .models import ToDo
# Create your views here.


def index(request):
    mytodo = ToDo.objects.order_by('id')
    form = ToDoForm()
    total = ToDo.objects.all().count()

    context = {'mytodo': mytodo, 'form': form, 'total':total}
    return render(request, 'todo_app/index.html', context)


@require_POST
def addNewToDo(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        my_new_todo = ToDo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')


def completeToDo(request, todo_id):
    mytodo = ToDo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('index')


def deleteToDo(request):
    ToDo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    ToDo.objects.all().delete()
    return redirect('index')