from product.models import product

CART_SESSION_ID='cart'

class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            Product = product.objects.get(id=int(item['id']))
            item['product'] = Product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(Product.id,item['color'],item['size'])
            yield item



    def unique_id_generator(self,id,color,size):
        result = f'{id}-{color}-{size}'
        return result

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def add(self,Product,quantity,color,size):
        unique = self.unique_id_generator(Product.id,color,size)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0,'price': int(Product.price),'color': color,'size': size,'id': str(Product.id)}

        self.cart[unique]['quantity'] += int(quantity)

        self.save()

    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total
    def delete(self,id):
        if id in self.cart:
            del self.cart[id]
            self.save()



    def save(self):
        self.session.modified = True

