from django.shortcuts import render, redirect
from .models import Car_Db, Category_Db
from Web_Pages.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def main_page(request):
    return render(request, 'mainpage.html')


def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_image = request.FILES['category_image']
        cat_obj = Category_Db(category_name=category_name, category_image=category_image)
        cat_obj.save()
        messages.success(request, "Category added")
        return redirect(add_category)

    return render(request, 'add_category.html')


def display_category(request):
    category = Category_Db.objects.all()
    context = {
        "category": category
    }
    return render(request, 'display_category.html', context)


def edit_category(request, id):
    data = Category_Db.objects.get(id=id)
    context ={
        "data": data
    }
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        try:
            categery_image = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(categery_image.name, categery_image)
        except MultiValueDictKeyError:
            file = Category_Db.objects.get(id=id).category_image
        Category_Db.objects.filter(id=id).update(category_name=category_name, category_image=file)
        messages.warning(request, "Category Updated!")
        return redirect(display_category)

    return render(request, 'edit_category.html', context)


def delete_category(request, id):
    data = Category_Db.objects.filter(id=id)
    data.delete()
    messages.error(request, "Category Deleted!")
    return redirect(display_category)


def add_car(request):
    if request.method == "POST":
        car_name = request.POST.get('carname')
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
        created_date = request.POST.get('date')
        
        car = Car_Db(car_name=car_name, car_brand=car_brand, state=state, city=city, color=color, model=model, 
                     year=year, condition=condition, price=price, description=description, car_photo=car_photo, body_style=body_style, 
                     engine=engine, transmission=transmission, kilometers=kilometers, milage=milage, fuel_type=fuel_type,
                     no_of_owners=no_of_owners,created_date=created_date)
        car.save()
        messages.success(request, "Car added")
        return redirect(add_car)
    
    return render(request, 'add_car.html')


def display_car(request):
    cars = Car_Db.objects.all()
    context = {
        "cars": cars
    }
    return render(request, 'display_car.html', context)


def edit_car(request, id):
    category = Category_Db.objects.all()
    cars = Car_Db.objects.get(id=id)
    context = {
        "category": category,
        "cars": cars
    }
    if request.method == "POST":
        car_name = request.POST.get('carname')
        car_brand = request.POST.get('carbrand')
        state = request.POST.get('state')
        city = request.POST.get('city')
        color = request.POST.get('color')
        model = request.POST.get('model')
        year = request.POST.get('year')
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        description = request.POST.get('description')
        body_style = request.POST.get('bodystyle')
        engine = request.POST.get('engine')
        transmission = request.POST.get('transmission')
        kilometers = request.POST.get('kilometers')
        milage = request.POST.get('milage')
        fuel_type = request.POST.get('fuel')
        no_of_owners = request.POST.get('owners')
        created_date = request.POST.get('date')
        try:
            car_photo = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(car_photo.name, car_photo)
        except MultiValueDictKeyError:
            file = Car_Db.objects.get(id=id).car_photo
        
        Car_Db.objects.filter(id=id).update(car_name=car_name, car_brand=car_brand, state=state, city=city, color=color, model=model, 
                     year=year, condition=condition, price=price, description=description, car_photo=file, body_style=body_style, 
                     engine=engine, transmission=transmission, kilometers=kilometers, milage=milage, fuel_type=fuel_type,
                     no_of_owners=no_of_owners,created_date=created_date)
        messages.warning(request, "Car Updated!")
        return redirect(display_car)

    return render(request, 'edit_car.html', context)


def delete_car(request, id):
    car = Car_Db.objects.filter(id=id)
    car.delete()
    messages.error(request, "Car Deleted!")
    return redirect(display_car)
    

def admin_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        if User.objects.filter(username__contains=u_name).exists():
            user = authenticate(username=u_name, password=p_word)
            if user is not None:
                login(request, user)
                request.session['username'] = u_name
                request.session['password'] = p_word
                messages.success(request, "Logged In Successfully")
                return redirect(main_page)
            else:
                messages.error(request, "Login Failed!")
                return redirect(admin_login)
        else:
            messages.error(request, "User Not Exist!")
            return redirect(admin_login)

    return render(request, 'admin_login.html')


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged Out Successfully")
    return redirect(admin_login)


def contact(request):
    data = ContactDB.objects.all()
    context = {"data": data}
    return render(request, 'display_contact.html', context)


def delete_contact(request, id):
    data = ContactDB.objects.filter(id=id)
    data.delete()
    messages.error(request, "Contact Request Deleted!")
    return redirect(contact)


def display_enquiry(request):
    enq_data = EnquiryDB.objects.all()
    context = {"enq_data": enq_data}
    return render(request, 'display_enquiry.html', context)


def delete_enquiry(request, id):
    enq_data  = EnquiryDB.objects.filter(id=id)
    enq_data.delete()
    messages.error(request, "Enquiry Request Deleted!")
    return redirect(display_enquiry)


def display_testdrive(request):
    test_data = TestDriveDB.objects.all()
    context = {"test_data": test_data}
    return render(request, 'display_testdrive.html', context)


def delete_testdrive(request, id):
    test_data  = TestDriveDB.objects.filter(id=id)
    test_data.delete()
    messages.error(request, "Test Drive Request Deleted!")
    return redirect(display_testdrive)