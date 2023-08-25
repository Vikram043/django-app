# from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render, redirect,get_object_or_404
from .models import Dish, Order, OrderQuantity
def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST['dish_name']
        price = request.POST['price']
        availability = request.POST.get('availability', False)
        # Dish.objects.create( price=12.99, availability=True)
        availability=True if availability=="on"  else False
     
        Dish.objects.create(dish_name=dish_name, price=float(price), availability=availability)
        return redirect('dish_list')

    return render(request, 'add_dish.html')

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})
def remove_dish(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    dish.delete()
    return redirect('dish_list')
def remove_order(request, dish_id):
    order = Order.objects.get(id=dish_id)
    order.delete()
    return redirect('display_order')
def update(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    
    if request.method == 'POST':
        dish.dish_name = request.POST.get('dish_name')
        dish.price = float(request.POST.get('price'))
        dish.availability =True if request.POST.get('availability') == 'on' else False
        print(request.POST.get('availability'))
        dish.save()
      
        return redirect('dish_list')
    
    return render(request, 'edit.html', {'dish': dish})



def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        # Update the order status or other details here
        order.status = request.POST.get('status')
        print( "change",request.POST.get('status'))
        order.save()
        return redirect('display_orders')
    
    return render(request, 'update_order.html', {'order': order})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    # get_object_or_404(OrderQuantity, pk=order_id).delete()
    order.delete()
    return redirect('display_orders')
    
    # return render(request, 'cancel_order.html', {'order': order})

# views.py

def take_order(request, dish_id):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        selected_dish_ids = [int(dish_id) for dish_id in request.POST.getlist('selected_dishes[]')]
        quantities = [int(quantity) for quantity in request.POST.getlist('dish_quantity[]')]

        selected_dishes = Dish.objects.filter(id__in=selected_dish_ids)
        
        if selected_dishes.exists():
            new_order = Order(cutomer_name=customer_name)
            new_order.save()

            for dish, quantity in zip(selected_dishes, quantities):
                if quantity > 0:
                    order_quantity = OrderQuantity(order=new_order, dish=dish, quantity=quantity,dish_name=dish)
                    order_quantity.save()

            new_order.save()

        return redirect('display_orders')

    menu = Dish.objects.all()
    return render(request, 'take_order.html', {'menu': menu})



# zomato/views.py

def display_orders(request):
    orders = Order.objects.all()
    quantity = OrderQuantity.objects.all()
   
    return render(request, 'display_orders.html', {'orders': orders})