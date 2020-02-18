from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='list'),
	path('update/<str:primekey>/', views.updatetask, name='update'), #names have to be the same as what the name is in the templates
	path('delete/<str:primekey>/', views.deletetask, name = 'delete'),
]