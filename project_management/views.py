from django.shortcuts import redirect, render
from django.views import View
from .models import Project, Tasks
from .forms import ProjectForm, TasksForm


# Create your views here.

class HomeView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'core/index.html', {'projects': projects})

class AddProject(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'core/add_project.html', {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = ProjectForm()
        return render(request, 'core/add_project.html', {'form': form})

class DeleteProject(View):
    def post(self, request):
        data = request.POST
        project_id = data.get('id')
        project = Project.objects.get(id=project_id)
        project.delete()
        return redirect('/')


class EditProject(View):
    def get(self,request,id):
        project = Project.objects.get(id=id)
        form = ProjectForm(instance=project)
        return render(request,'core/edit_project.html',{'form':form})

    def post(self,request,id):
        project = Project.objects.get(id=id)

        form = ProjectForm(request.POST,instance=project)    
        if form.is_valid():
            form.save()
            return redirect('/')


# This is view for task management
class TaskHomeView(View):
    def get(self, request):
        tasks = Tasks.objects.all()
        return render(request, 'core/task.html', {'tasks': tasks})

class AddTask(View):
    def get(self, request):
        form = TasksForm()
        return render(request, 'core/add_task.html', {'form': form})
    
    def post(self, request):
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request, 'core/add_task.html', {'form': form})

class DeleteTask(View):
    def post(self, request):
        data = request.POST
        task_id = data.get('id')
        task = Tasks.objects.get(id=task_id)
        task.delete()
        return redirect('task')

class EditTask(View):
    def get(self,request,id):
        task = Tasks.objects.get(id=id)
        form = TasksForm(instance=task)
        return render(request,'core/edit_task.html',{'form':form})

    def post(self,request,id):
        task = Tasks.objects.get(id=id)

        form = TasksForm(request.POST,instance=task)    
        if form.is_valid():
            form.save()
            return redirect('task')

        