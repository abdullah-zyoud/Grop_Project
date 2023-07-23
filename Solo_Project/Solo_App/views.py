from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car ,User
from django.contrib import messages


def index(request): 
    return render(request, 'home.html')
def regLog(request): 
    return render(request, 'index.html')

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/regLog')
    else:
        User.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        return redirect ('/regLog')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/regLog')
    else:
       
        this_user = User.objects.get(email=request.POST['email2'])
        request.session['user_id'] = this_user.id
        request.session['username']=this_user.username
        if this_user.isAdmin==1 : 
            return redirect ('/admin') 
        else :
            return redirect('/user')
    
def admin(request): 
    context = {
        'username' : request.session['username'],
        'cars': Car.objects.all(),
    }
    return render(request, 'admin.html', context)
 
def user(request): 
    context = {
        'username' : request.session['username'],
        'cars': Car.objects.all(),
    }
    return render(request, 'user.html', context) 

def add(request):
    return render(request, 'add.html')

def addCar(request):
    errors = Car.objects.addValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')
    else:
    
        Car.objects.create(
                        name = request.POST['name'], 
                        model = request.POST['model'], 
                        color = request.POST['color'],
                        fuelType = request.POST['fuelType'],
                        price = request.POST['price'],
                        user = User.objects.get(id=request.session['user_id']), 
                    )
        return redirect('/admin')

def edit(request, car_id):
    context = {
        'cars' : Car.objects.get(id=car_id) 
    }
    return render(request,'edit.html',context)

def editCar(request, car_id):
    errors = Car.objects.editValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{car_id}')
    else:
   

        selected = Car.objects.get(id=car_id)
        selected.name = request.POST['name']
        selected.model = request.POST['model']
        selected.color = request.POST['color']
        selected.fuelType = request.POST['fuelType']
        selected.price = request.POST['price']
        selected.save()
        return redirect('/admin')

def delete(request, car_id):
    dell = Car.objects.get(id = car_id)
    dell.delete() 
    return redirect('/admin')

def book(request): 
    return render(request, 'book.html')


def logout(request): 
    request.session.flush()
    return redirect('/')
