from django.shortcuts import render, redirect
from .models import Car_Db

# Create your views here.
def main_page(request):
    return render(request, 'mainpage.html')


def add_car(request):
    return render(request, 'add_car.html')

def save_car(request):
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
        return redirect(add_car)