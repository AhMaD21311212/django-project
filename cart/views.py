from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product.models import product
from .cart_model import Cart
from .models import Order, OrderItem,DiscountCode


class cartdetailView(LoginRequiredMixin,View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class cartAddView(View):
    def post(self, request, pk):
        Product = get_object_or_404(product, id=pk)
        quantity, color, size = request.POST.get('quantity'), request.POST.get('color', 'empty'), request.POST.get(
            'size', 'empty')
        cart = Cart(request)
        cart.add(Product, quantity, size, color)
        return redirect("cart:cart_detail")


class cartDelete(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        print(id)
        return redirect('cart:cart_detail')


class OrderDetailView(LoginRequiredMixin,View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request,'cart/order_detail.html',{'order': order})


class OrderCreationView(LoginRequiredMixin,View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, Product=item['product'], size=item['size'], color=item['color'],
                                     quantity=item['quantity'],price=item['price'])

        cart.remove_cart()

        return redirect('cart:Order-Detail',order.id)



class Apply(LoginRequiredMixin,View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect('cart:Order-Detail', order.id)

        order.total_price -= order.total_price * discount_code.discount/100
        order.save()

        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:Order-Detail', order.id)

