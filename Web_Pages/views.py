from django.shortcuts import render, redirect
from Admin_app.models import Category_Db, Car_Db
from django.contrib import messages
from .models import UserDB


# Create your views here.
def home(request):
    category = Category_Db.objects.all()
    featured = Car_Db.objects.filter(is_featured=True)
    context = {
        "category": category,
        "featured": featured
    }
    return render(request, 'home.html', context)


def cars(request, car_name):
    car = Car_Db.objects.filter(car_category=car_name)
    context = {
        "car": car,
    }
    return render(request, 'cars.html', context)

def all_cars(request):
    car = Car_Db.objects.all()
    context = {
        "car": car,
    }
    return render(request, 'cars.html', context)

def car_detail(request, id):
    single_car = Car_Db.objects.get(id=id)
    context = {"single_car": single_car}
    return render(request, 'car_detail.html', context)

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        obj = UserDB(username=username, email=email, password=password, confirm_password=confirm)
        obj.save()
        messages.success(request, "Registered Successfully")
        return redirect(user_login)

    return render(request, 'user_register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if UserDB.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            messages.success(request, "Logged In Successfully")
            return redirect(home)
        else:
            messages.error(request, "Login Failed!")
            return redirect(user_login)

    return render(request, 'user_login.html')


def user_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request, "Logged Out Successfully")
    return redirect(user_login)