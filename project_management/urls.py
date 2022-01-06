from django.urls import path
from .views import HomeView, AddProject, DeleteProject, EditProject
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('delete_project/', DeleteProject.as_view(), name='delete_project'),
    path('edit_project/<int:id>/', EditProject.as_view(), name='edit_project'),
    ]

