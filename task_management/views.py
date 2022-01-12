from django.shortcuts import redirect, render
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.

class TaskHomeView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task/task.html', {'tasks': tasks})

class AddTask(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task/add_task.html', {'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task/')
        return render(request, 'task/add_task.html', {'form': form})

class DeleteTask(View):
    def post(self, request):
        data = request.POST
        task_id = data.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task/')

class EditTask(View):
    def get(self,request,id):
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)
        return render(request,'task/edit_task.html',{'form':form})

    def post(self,request,id):
        task = Task.objects.get(id=id)

        form = TaskForm(request.POST,instance=task)    
        if form.is_valid():
            form.save()
            return redirect('task/')
