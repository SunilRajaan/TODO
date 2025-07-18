from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForms
from .AI import create_description_with_ai
import json
# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            name = request.POST.get('name')        
            description = request.POST.get('description')        
            status = request.POST.get('status')      

            Todo.objects.create(name=name, description=description, status=status) 
            return redirect('home')
        elif action == 'generate':
            name = request.POST.get('name')
            status = request.POST.get('status')
            generated_description = create_description_with_ai(name)
            dict_generated_description = json.loads(generated_description)
            return render(request, 'create.html', context={'generated_description':dict_generated_description('description'), 'name':name})
    return render(request, 'create.html')


def edit_todo(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    form = TodoForms(instance=todo_obj)
    if request.method == 'POST':
        form = TodoForms(instance=todo_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'edit.html', context={'form':form})

def delete_todo(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')
