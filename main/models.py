from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model


User =get_user_model()


class Profile(models.Model):
            
                #Linking the fk to the use models that is imported
                user =models.ForeignKey(User, on_delete=models.CASCADE)
                
            
            
                fname=models.CharField(max_length=200)
                
                lname=models.CharField(max_length=200)
                
            
                email =models.EmailField(blank=True)
            
                number =models.CharField(max_length=200)
            
                address =models.CharField(max_length=200, blank=True)
            
                Dob =models.DateField(blank=True, null=True)
                 
                #To add a default profile 
                #We use default attribute
                profile_img  =models.ImageField(upload_to='profile',default ='blank.png',blank=True)
            
                
            
            
            
                def __str__(self):
            
                    return self.user.username


#catergory

class Category(models.Model):
     name =models.CharField(max_length=50)

     def __str__(self):
        return self.name
     #To change the class name we
     class Meta:
          verbose_name_plural = 'Categories'
          
#product
class Product(models.Model):
    name =models.CharField(max_length=100)
    price =models.DecimalField(default=0,decimal_places =2 ,max_digits =10 )
    category =models.ForeignKey(Category,on_delete =models.CASCADE,default =1) 
    description =models.CharField(max_length=250, default = '',blank =True)
    Image =models.ImageField(upload_to='uploads/product/')

    def __str__(self):
         return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user.username})"
    
    
    def get_total_price(self):
        total = 0
        for item in self.items.all():  # items is related_name in CartItem
            total += item.product.price * item.quantity
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"