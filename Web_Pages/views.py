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
    car = Car_Db.objects.filter(is_approved=True)
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


def add_listing(request):
    if request.method == "POST":
        car_name = request.POST.get('carname')
        car_category = request.POST.get('category')
        car_brand = request.POST.get('brand')
        state = request.POST.get('state')
        city = request.POST.get('city')
        color = request.POST.get('color')
        model = request.POST.get('model')
        year = request.POST.get('year')
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        description = request.POST.get('description')
        car_photo = request.FILES['image']
        body_style = request.POST.get('bodystyle')
        engine = request.POST.get('engine')
        transmission = request.POST.get('transmission')
        kilometers = request.POST.get('kilometers')
        milage = request.POST.get('milage')
        fuel_type = request.POST.get('fuel')
        no_of_owners = request.POST.get('owners')
        is_featured = request.POST.get('featured')
        is_approved = request.POST.get('aprooved')
        created_date = request.POST.get('date')

        car = Car_Db(car_name=car_name, car_category=car_category, car_brand=car_brand, state=state, city=city, color=color, model=model, 
                     year=year, condition=condition, price=price, description=description, car_photo=car_photo, body_style=body_style, 
                     engine=engine, transmission=transmission, kilometers=kilometers, milage=milage, fuel_type=fuel_type,
                     no_of_owners=no_of_owners, is_featured=is_featured, is_approved=is_approved, created_date=created_date)
        car.save()
        messages.warning(request, "Successful!.. Car will be listed After Varificaton")
        return redirect(add_listing)

    category = Category_Db.objects.all()
    context = {"category": category}
    return render(request, 'add_listing.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone_number')
        subject = request.POST.get('msg_subject')
        message = request.POST.get('message')
        contact = ContactDB(name=name, email=email, mobile=mobile, subject=subject, message=message)
        contact.save()
        messages.success(request, "Our Sales Executive will contact you shortly..")
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
        car_id = request.POST.get('car_id')
        car_name = request.POST.get('car_name')
        name = request.POST.get("enq_name")
        email = request.POST.get("enq_email")
        message = request.POST.get("enq_message")
        obj = EnquiryDB(car_id=car_id, car_name=car_name, name=name, email=email, message=message)
        obj.save()
        messages.success(request, "Our Sales Executive will contact you shortly..")
        return redirect('/car_detail/'+car_id)


def testdrive(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        car_name = request.POST.get('carname')
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        day = request.POST.get("day")
        time = request.POST.get("time")
        obj = TestDriveDB(car_id=car_id, car_name=car_name, name=name, email=email, mobile=mobile, preferred_day=day,
                           preferred_time=time)
        obj.save()
        messages.success(request, "Successfully Booked Test Drive")
        return redirect('/car_detail/'+car_id)
    
