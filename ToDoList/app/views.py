from django.shortcuts import render, redirect
from .models import Todolist
# Create your views here.
def main(request):
    todolists = Todolist.objects.all()
    return render(request, 'main.html', {'todolists':todolists})

def new(request):
    
    if request.method =='POST':
        new_todolist=Todolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            status=request.POST['status'],
            due=request.POST['due']
        )
        return redirect('detail', new_todolist.id)
    return render(request, 'new.html')

def detail(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)
    return render(request, 'detail.html',{'todolist':todolist})

def update(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)

    if request.method =='POST':
        Todolist.objects.filter(id=todolist_id).update(
                title=request.POST['title'],
                content=request.POST['content'],
                status=request.POST['status'],
                due=request.POST['due']
        )
        return redirect('detail', todolist_id)
    return render(request, 'update.html',{'todolist':todolist})

def delete(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)
    todolist.delete()
    return redirect('/')