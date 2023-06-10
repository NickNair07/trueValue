from django.shortcuts import render, redirect
from Admin_app.models import Category_Db, Car_Db
from .models import *
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone_number')
        subject = request.POST.get('msg_subject')
        message = request.POST.get('message')
        contact = ContactDB(name=name, email=email, mobile=mobile, subject=subject, message=message)
        contact.save()
        return redirect('contact')
    
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
    

def enquiry(request):
    if request.method == "POST":
        name = request.POST.get("enq_name")
        email = request.POST.get("enq_email")
        message = request.POST.get("enq_message")
        obj = EnquiryDB(name=name, email=email, message=message)
        obj.save()
        return redirect('car_detail', id=id)


def testdrive(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        day = request.POST.get("day")
        time = request.POST.get("time")
        obj = TestDriveDB(name=name, email=email, mobile=mobile, preferred_day=day,
                           preferred_time=time)
        obj.save()
        return redirect('car_detail', id=obj.id)