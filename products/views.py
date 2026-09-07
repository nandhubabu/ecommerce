from django.shortcuts import redirect, render
from orders.models import Order, OrderItem
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order_item, created = OrderItem.objects.get_or_create(product=product, order=order)

    return redirect('cart')

def cart_view(request):
    order, created = Order.objects.get_or_create(user=request.user)
    cart_items = OrderItem.objects.filter(order=order)
    return render(request, 'products/cart.html', {'cart_items': cart_items})