from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from .form import formPerson

@login_required
def persons_list(request):
    data = {}
    data['persons'] = Person.objects.all()
    return render(request, 'Clients/persons_list.html', data)

@login_required
def update(request , pk):
    data = {}
    person = Person.objects.get(pk=pk)
    form = formPerson(request.POST or None, request.FILES or None , instance=person)

    if form.is_valid():
        form.save()
        return redirect ('url_persons_list')    
    
    data['form'] = form
    data['person'] = person
    return render(request , 'Clients/form.html' , data)

@login_required
def create (request):
    data = {}
    form = formPerson(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect ('url_persons_list')  
    
    data['form'] = form
    return render(request , 'Clients/form.html' , data)

@login_required
def delete(request , pk):
    person = Person.objects.get(pk=pk)
    person.delete()
    return redirect('url_persons_list')