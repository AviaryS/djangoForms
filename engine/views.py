from django.http import HttpResponse
from django.shortcuts import render
from .forms import OrderForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        service = request.POST.get("service", None)
        text = request.POST.get('text', None)

    return render(request, 'engine/index.html', context={'name': name, 'email': email, 'phone': phone, 'service': service, 'text': text})


def form(request):
    return render(request, 'engine/form.html')


def order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        country = request.POST.get('country', None)
        city = request.POST.get('city', None)
        street = request.POST.get('street', None)
        number_of_house = request.POST.get('number_of_house', None)

        result = f"""<p>{first_name} {last_name}, проверьте адрес доставки:</p>
        <p>{country}</p>
        <p>{city}</p>
        <p>{street} {number_of_house}</p>
        """
        return HttpResponse(result)
    else:
        Form = OrderForm()
        return render(request, 'engine/order.html', {'form': Form})
