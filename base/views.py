from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForms

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


def edit_todo(request):
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForms()
    return render(request, 'edit.html', context={'form':form})