from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
	things = Task.objects.all()
	count = Task.objects.all().count()
	countcomplete = Task.objects.filter(complete=True).count()

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		print('it happened')
		if form.is_valid():
			form.save()
		return redirect('/')

	if count == 0:
		percent = 100
	else:
		percent = countcomplete/count * 100

	remainder = count - countcomplete

	context = {'tasks':things, 'form':form, 'total':count, 'done':countcomplete, 'percent':percent, 'remainder':remainder}

	return render(request, 'tasks/list.html', context)

def updatetask(request, primekey):
	item = Task.objects.get(id=primekey)

	form = TaskForm(instance=item)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'tasks/update.html', context)

def deletetask(request, primekey):
	item = Task.objects.get(id=primekey)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html',context)