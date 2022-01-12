from django.urls import path
from .views import HomeView, AddProject, DeleteProject, EditProject, TaskHomeView, AddTask, DeleteTask, EditTask
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('delete_project/', DeleteProject.as_view(), name='delete_project'),
    path('edit_project/<int:id>/', EditProject.as_view(), name='edit_project'),
    path('task/', TaskHomeView.as_view(), name='task'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('delete_task/', DeleteTask.as_view(), name='delete_task'),
    path('edit_task/<int:id>/', EditTask.as_view(), name='edit_task'),
]

