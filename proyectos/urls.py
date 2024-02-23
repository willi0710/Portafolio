from django.urls import path
from .views import project_render


app_name = 'proyectos'
urlpatterns =[
    path('', project_render, name= 'project' )
]