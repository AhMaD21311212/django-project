from django.urls import path
from . import views


app_name = 'cart'

urlpatterns =[
    path('detail',views.cartdetailView.as_view(),name='cart_detail'),
    path('add/<int:pk>',views.cartAddView.as_view(),name='cart_add'),
    path('add/<str:id>',views.cartDelete.as_view(),name='cart_delete'),
    path('Order/<int:pk>',views.OrderDetailView.as_view(),name='Order-Detail'),
    path('Order/creation',views.OrderCreationView.as_view(),name='Order-Creat'),
    path('Apply/<int:pk>',views.Apply.as_view(),name='apply_discount'),
]