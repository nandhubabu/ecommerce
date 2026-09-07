from django.shortcuts import redirect
from orders.models import OrderItem
from django.shortcuts import render
from .models import Product,Order

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    order, create = Order.objects.get_or_create(user = request.user)
    order_item , created = OrderItem.objects.get_or_create(product = product ,order  = order )

    return redirect('cart')