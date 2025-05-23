from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        total_count = cart.items.count()  # number of distinct items
        
        return {'cart_item_count': total_count}
    return {'cart_item_count': 0}
