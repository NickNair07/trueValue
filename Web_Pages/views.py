from django.shortcuts import render, get_object_or_404
from Admin_app.models import Category_Db, Car_Db
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
    paginator_obj = Paginator(car, 3)
    page = request.GET.get('page')
    paged_cars = paginator_obj.get_page(page)
    context = {
        "car": paged_cars,
    }
    return render(request, 'cars.html', context)

def car_detail(request, id):
    single_car = get_object_or_404(Car_Db, id=id)
    context = {"single_car": single_car}
    return render(request, 'car_detail.html', context)

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
