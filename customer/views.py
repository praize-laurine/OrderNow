from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'customer/index.html')

def about(request):
    return render(request, 'customer/about.html')    

def order(request):
    # get every every item from each category
    appetizers = MenuItem.objects.filter(category__name__contains = 'Appetizer')
    entres = MenuItem.objects.filter(category__name__contains = 'Entre')
    desserts = MenuItem.objects.filter(category__name__contains = 'Dessert')
    drinks = MenuItem.objects.filter(category__name__contains = 'Drink')


    # pass into context
    context = {
        'appetizers': appetizers,
        'entres': entres,
        'desserts': desserts,
        'drinks': drinks
    }
    # render template
    return render(request, 'customer/order.html', context)

def post(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    street = request.POST.get('street')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip_code')

    order_items = {
        'items': []
    }

    items = request.POST.getlist('items[]')

    for item in items:
        menu_item = MenuItem.objects.get(pk__contains = int(item))
        item_data = {
            'id' : menu_item.pk,
            'name': menu_item.name,
            'price': menu_item.price
        }

        order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price = price,
                name = name,
                email = email,
                street = street,
                city = city,
                state = state,
                zip_code = zip_code
                )
            order.items.add(*item_id)

            # send confirmation email
            body = ('Thank you for your order. Your food is being made and would be delivered soon\n'
            f'You total: {price}\n'
            'Thank you again for your order!')

            send_mail(
                'Thank You For Your Order',
                body,
                'example@gmail.com',
                [email],
                fail_silently = False
            )

            context = {
                'items': order_items['items'],
                'price': price
            }

    return render(request, 'customer/order_confirmation.html', context)
