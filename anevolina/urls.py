from django.urls import path
from anevolina import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.project_details, name='project_details')
]