from django.contrib import admin

# Register your models here.
from . models import Profile,Category,Product,CartItem,Cart




admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

