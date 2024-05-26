from django.urls import path
from . import views

app_name ='product'
urlpatterns = [
    path('<int:pk>',views.productdetailView.as_view(),name ="product_detail"),
    path('Navbar',views.NavbarpartialView.as_view(),name ="navbar"),
    path('all',views.ProductListView.as_view(),name ="product_list"),
    path('<slug:slug>',views.CategoryDetailView,name ="category_detail"),
]