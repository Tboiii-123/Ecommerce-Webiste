from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login ,logout

from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile,Product,Category,Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import JsonResponse
import yagmail
import threading
import stripe
from django.conf import settings
import os
import datetime

stripe.api_key =os.getenv('STRIPE_SECRET_KEY')
# Create your views here.



#Login Method
def Login(request):
    

    if request.method =="POST":
            
            username =request.POST.get("user")
            password =request.POST.get("password")

            user =authenticate(request,username =username , password =password)
            if user is not None:
                login(request,user)
                messages.success(request,'You have been logged in Successfully!!!!!!')

                return redirect('profile')
                
            else:
                messages.error(request,'There was an error when logging in,Please Login in again!!!!!')
                
                return redirect('login')
            
    return render(request,'login.html',{

                })

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('fname') or ''
        lastname = request.POST.get('lname') or ''
        username = request.POST.get('username') or ''
        number = request.POST.get('number') or ''
        email = request.POST.get('email') or ''
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([firstname, lastname, username, number, email, password1, password2]):
            messages.error(request, "All entries must be filled.")
            return render(request, 'register.html', {
                'fname': firstname,
                'lname': lastname,
                'username': username,
                'number': number,
                'email': email,
            })

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please try again.")
            return render(request, 'register.html', {
                'fname': firstname,
                'lname': lastname,
                'username': username,
                'number': number,
                'email': email,
            })

        elif password1 != password2:
            messages.error(request, "Make sure your password matches.")
            return render(request, 'register.html', {
                'fname': firstname,
                'lname': lastname,
                'username': username,
                'number': number,
                'email': email,
            })

        else:
            try:
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    password=password1,
                    email=email
                )
                Profile.objects.create(
                    user=user,
                    fname=firstname,
                    lname=lastname,
                    email=email,
                    number=number,
                )
                messages.success(request, "You have registered successfully.")
                return redirect('login')

            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}. Please try again.")
                return render(request, 'register.html', {
                    'fname': firstname,
                    'lname': lastname,
                    'username': username,
                    'number': number,
                    'email': email,
                })

    return render(request, 'register.html')


#Logout
def Logout(request):
     
     logout(request)
     messages.success(request,'Logged out sucessfully.....')
    

     return redirect ("login")



#Main Page
@login_required(login_url='/login/')
def index(request):
    product =Product.objects.all()
    product2 =list(Product.objects.all())
    
    

    return render(request,'index.html',{
        'products':product[:4],
        'products2':product2[-4:]

        
    })


#Profile Page
@login_required(login_url='/login/')
def profile(request):


    
    profile =Profile.objects.get(user=request.user)
    
    if request.method == "POST":

        if request.FILES.get('image') == None:
            image =profile.profile_img

        else:
            
            image =request.FILES.get('image')
            
         # Date of Birth handling
        dob_input = request.POST.get('dob')
        if dob_input:
            try:
                dob = request.POST.get('dob')
            except ValueError:
                dob = None  # or handle invalid date input separately
        else:
            dob = None
        number =request.POST.get('number') or None
        address =request.POST.get('address') or None
        email =request.POST.get('email')     or None   
        profile.profile_img =image        
        profile.Dob =dob
        profile.number= number
        profile.address =address
        profile.email =email      
        profile.save()

        return redirect('profile')

    return render(request,'profile.html',{
         'profile':profile
         

    })



#Products page
@login_required(login_url='/login/')
def product(request,pk):
    product =Product.objects.get(id=pk)
    product_category =product.category

    # Get related products: same category, but exclude the current product
    related_products = Product.objects.filter(category=product_category).exclude(id=product.id)[:4]  # Limit to 4
    
    item_quantity = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.filter(cart=cart, product=product).first()
            if cart_item:
                item_quantity = cart_item.quantity
        except Cart.DoesNotExist:
            pass
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quantity = int(data.get('quantity', 1))  # changed key to 'quantity'

            product = get_object_or_404(Product, id=pk)
            cart, _ = Cart.objects.get_or_create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()

            total_count = sum(item.quantity for item in cart.items.all())

            return JsonResponse({'success': True, 'cart_item_count': total_count})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


    return render(request,'product.html',{
        'product':product ,
        'relateds':related_products ,
           'item_quantity': item_quantity,   
    })


     

#Category Page for Product
#The same as product page but using the seatch method.POST

@login_required(login_url='/login/')
def category(request):
    # foo =foo.replace('-',' ')

    if request.method =="POST":
        name =request.POST.get('searched')   
        
        # category = get_object_or_404(Category, name__iexact=name)
        categories = Category.objects.filter(name__icontains=name)
        category = categories.first() if categories.exists() else None

        products =Product.objects.filter(category=category)

 
    return render (request,'category.html',{
            'products':products,
            'category':category

        })


#Category link also for the product pages
@login_required
def category_link(request,item):

    category =Category.objects.get(name=item)

    products =Product.objects.filter(category=category)
    
        
    return render(request, 'category.html', {
        'products':products,
        'category':category
            
    })

    
    


#Add to cart method.using json
@login_required(login_url='/login/')
def add_to_cart(request, product_id):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quantity = int(data.get('quantity', 1))  # changed key to 'quantity'

            product = get_object_or_404(Product, id=product_id)
            cart, _ = Cart.objects.get_or_create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()

            total_count = sum(item.quantity for item in cart.items.all())

            return JsonResponse({'success': True, 'cart_item_count': total_count})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})




#Cart Page
@login_required(login_url='/login/')
def view_cart(request):
    cart_items = []
    

    


    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.select_related('product') 
             # fetch product info too

            cart_total = sum(item.quantity * item.product.price for item in cart_items)
            
            for item in cart_items:
                 item.product_total = item.quantity * item.product.price  # total price per product



        except Cart.DoesNotExist:
            pass
    return render(request, 'cart.html',
                   {'cart_items': cart_items,
                    'cart_total':cart_total,
                    
                    }
                   
                   )





#Navigation bar 

def navbar(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    total_count = cart.items.count()  # number of distinct items
        
    return render(request, 'nav.html', {'cart_item_count': total_count})


#Diditing in the cart
@login_required(login_url='/login/')
def cart_action(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)

        

        action = request.POST.get('action')

        if action == 'update':
            new_quantity = int(request.POST.get('quantity', 1))
            cart_item.quantity = new_quantity
            cart_item.save()

        elif action == 'delete':
            cart_item.delete()

        return redirect('/cart/')  # or use: return redirect('cart')







#Cehckout Phase

@login_required(login_url='/login/')
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return redirect('view_cart')

    if not cart.items.exists():
        messages.error(request, 'No item in the cart. Please add items.')
        return redirect('view_cart')

    amount = int(cart.get_total_price() * 100)

    # Stripe maximum amount is 999,999.99 in cents
    if amount > 99999999:
        messages.error(request, "Total amount exceeds Stripe's limit of $999,999.99.")
        return redirect('view_cart')

    if request.method == 'GET':
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            metadata={'user_id': request.user.id}
        )
        cart.items.all().delete()
        return render(request, 'checkout.html', {
            'client_secret': intent.client_secret,
            'stripe_publishable_key': os.getenv('STRIPE_PUBLISHABLE_KEY'),
            'amount': amount / 100,
        })

    if request.method == 'POST':
        payment_intent_id = request.POST.get('payment_intent_id')
        if not payment_intent_id:
            messages.error(request, "Payment ID missing.")
            return redirect('checkout')

        intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        if intent.status == 'succeeded':
            cart.items.all().delete()
            messages.success(request, 'Payment successful!')
            return redirect('checkout')
        else:
            messages.error(request, "Payment not completed. Please try again.")
            return redirect('checkout')




passwordName ='ancn ggqu qxlh rbnt'

main_mail ="tayelawal775@gmail.com"



#Function for the news letter using the threading method for fasters process
def send_mail(request,mail):
    try:
        body=f'''Hi {request.user}
            Thanks for subscribing to Hussein Sale Commerce,We hope you find and get updated prodyucts you will need in the nearest future
        '''

        yag =yagmail.SMTP(main_mail,passwordName)
        yag.send(
            to =mail,
            subject="A News Letter request",
            contents=[body],
            headers={"Reply-To":main_mail}
        )
        print("You'vs subscribed to our Newsletter successfully!!!!")

        
    except Exception as e:
        print('Failed to subscribed to our News Letter due to{e}.Please Subscribe Later')


#News Letter
@login_required(login_url='/login/')
def newsletter(request):

    try:

        if request.method =="POST":

            mail =request.POST.get('mail')


            threading.Thread(target=send_mail, args=(request,mail)).start()
            messages.success(request,("You'vs subscribed to our Newsletter successfully!!!!"))
        

    except Exception as e:
        messages.error(request,f'Failed to subscribed to our News Letter due to{e}.Please Subscribe Later')
        


    return redirect(request.META.get('HTTP_REFERER', '/'))



#Error Pge

def custom_404(request, exception):
    return render(request, 'error.html', status=404)

# views.py
def custom_500(request):
    return render(request, 'error.html', status=500)


