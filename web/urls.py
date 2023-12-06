from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('pay/', views.pay, name='pay'),
    path('payErro/', views.payErro, name='payErro'),
    path('payConfirm/', views.payConfirm, name='payConfirm'),
    path('products/', views.products, name='products'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/accounts/logout/',  LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'), 
]