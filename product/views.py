from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView,View

from product.models import product, Category, Size, Color


# Create your views here.


class productdetailView(DetailView):
    template_name = "product/product_detail.html"
    model = product


class NavbarpartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarpartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


#class ProductListView(ListView):
   # template_name = 'product/product_List.html'
    #queryset = product.objects.all()

    #def get_context_data(self, **kwargs):
    #    request = self.request
    #    colors = request.GET.getlist('color')
    #    sizes = request.GET.getlist('size')
    #    min_price = request.GET.get('min_price')
    #    max_price = request.GET.get('max_price')
    #    search_query = request.GET.get('q')
    #    queryset = product.objects.all()
    #    page_number = request.GET.get("page")
    #    pagination = Paginator(queryset, 1)
    #    object_list = pagination.get_page(page_number)
    #    if search_query:
    #        object_list = queryset.filter(title__icontains=search_query)
    #    if colors:
    #        object_list = queryset.filter(color__title__in=colors)
    #    if sizes:
    #        object_list = queryset.filter(size__title__in=sizes)
    #    if min_price and max_price:
    #        object_list = queryset.filter(price__lte=max_price, price__gte=min_price)

    #    context = super(ProductListView, self).get_context_data()
    #    #context['object_list'] = queryset
    #    context['object'] = object_list
    #    return context

class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = product
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()

        # دریافت پارامترهای جستجو از روی URL
        colors = self.request.GET.getlist('color')
        sizes = self.request.GET.getlist('size')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        if colors:
            queryset = queryset.filter(color__title__in=colors)

        if sizes:
            queryset = queryset.filter(size__title__in=sizes)

        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # افزودن پارامترهای جستجو به context
        #context['search_query'] = self.request.GET.get('search')
        context['colors'] = self.request.GET.getlist('color')
        context['sizes'] = self.request.GET.getlist('size')
        #context['min_price'] = self.request.GET.get('min_price')
        #context['max_price'] = self.request.GET.get('max_price')

        return context

#def article_list(request):
   # Product = product.objects.all()
    #page_number = request.GET.get("page")
    #pagination = Paginator(Product,1)
    #object_list = pagination.get_page(page_number)

    #return render(request, 'product/product_List.html', {'object': object_list})

def CategoryDetailView(request,slug):
    Product = product.objects.filter(slug=slug)

    return render(request,'product/category_detail.html', {'category':Product})

