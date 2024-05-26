from django.urls import path
from . import views


app_name = 'account'

urlpatterns =[
    path('login', views.UserLogin.as_view(),name='login'),
    path('register',views.registerView.as_view(), name='register'),
    path('randecode',views.randecodeView.as_view(), name="randecode"),
    path('logout',views.user_logout,name ="user_logout"),
    path('Address',views.AddAddressView.as_view(),name ="user_address"),
    path('Contact',views.ContacView,name ="Contact"),
    path('edit',views.Edit,name ="edit"),
]