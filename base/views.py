from django.shortcuts import render, redirect
from .models import Todo, TodoType
from .forms import TodoForms, TodoTypeForm

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')        
        description = request.POST.get('description')        
        status = request.POST.get('status')      

        Todo.objects.create(name=name, description=description, status=status) 
        return redirect('home')
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

# -------------------------------------Todo Types Views------------------------------------------------------------
def todo_types(request):
    todo = TodoType.objects.all()
    return render(request, "todo_types.html", {"todo": todo})

# Todo types create

def create_todo_types(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        TodoType.objects.create(
            name = name
            )
        return redirect('todo_types')
    return render(request, 'todo_type_create.html', context={"message": "Todo Type created successfully!"})

# update todo types
def edit_todo_types(request, pk):
    todo_type_obj = TodoType.objects.get(id=pk)
    form = TodoTypeForm(instance=todo_type_obj) #form object to handle the TodoType model # instance is used to pre-populate the form with existing data
    if request.method == "POST":
        form = TodoTypeForm(instance=todo_type_obj, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo_types')
    return render(request, 'todo_type_edit.html', context={"form": form})

def delete_todo_types(request, pk):
    todo_type_obj = TodoType.objects.get(id=pk)
    todo_type_obj.delete()
    return redirect('todo_types')