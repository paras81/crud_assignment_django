from django.urls import path
from .views import TaskHomeView, AddTask, DeleteTask, EditTask
urlpatterns = [

    path('task/', TaskHomeView.as_view(), name='home'),
    path('task/add_task/', AddTask.as_view(), name='add_task'),
    path('task/delete_task/', DeleteTask.as_view(), name='delete_task'),
    path('task/edit_task/<int:id>/',EditTask.as_view(),name='edit_task')

]