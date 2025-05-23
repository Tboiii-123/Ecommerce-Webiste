
from  django.urls import path
from . import views

urlpatterns = [
            path('',views.index, name='index'),
            path('login/',views.Login, name='login'),
            path('register/',views.register, name='register'),
            path('logout/',views.Logout, name='logout'),
            
            path('profile/',views.profile, name='profile'),
            path('product/<int:pk>',views.product , name ='product'),
    
        path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
        
         path('cart/', views.view_cart, name='view_cart'),
           path('navbar/', views.navbar, name='navbar'),
           path('cart/action/<int:item_id>/', views.cart_action, name='cart_action'),
           path('category/', views.category, name='category'),

           path('category/<str:item>/', views.category_link, name='category_link'),

           path('newsletter',views.newsletter, name='newsletter'),
           path('checkout/', views.checkout, name='checkout'),

           path('page_not_found/', views.custom_404, name='error'),
           


           
            

            
            
            
    ]

    