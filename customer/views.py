from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'customer/index.html')

def about(request):
    return render(request, 'customer/about.html')    

def Order(request):
    # get every every item from each category
    appetizers = MenuItem.objects.filter(category__name__contains = 'Appetizer')
    # main course = MenuItem.objects.filter(category__name__contains = 'Main course')
    desserts = MenuItem.objects.filter(category__name__contains = 'Dessert')
    drinks = MenuItem.objects.filter(category__name__contains = 'Drink')


    # pass into context
    context = {
        'appetizers': appetizers,
        # 'Main course': Main course,
        'desserts': desserts,
        'drinks': drinks
    }
    # render template
    return render(request, 'customer/order.html', context)

def post(request):
    order_items = {
        'items': []
    }

    items = request.POST.getlist('it3ems[]')

    for item in items:
        # menu_item = MenuItem.objects.get(pk_-contains = int(item))
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

            order = OrderModel.objects.create(price = price)
            order_items.add(*item_id)

            context = {
                'items': order_items['items'],
                'price': price
            }

    return render(request, 'customer/order_confirmation.html', context)
