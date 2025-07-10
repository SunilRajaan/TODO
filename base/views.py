from django.shortcuts import render
from .models import Todo

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
    return render(request, 'create.html')