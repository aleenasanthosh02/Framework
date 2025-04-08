from contextlib import redirect_stderr

from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
# Create your views here.

from .models import Book, Cart, CartItem


def listBook(request):

    books=Book.objects.all()
    paginator=Paginator(books, 4)
    page_number = request.GET.get('page')
    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'user/userlistbook.html',{'books':books,'page':page})

def detailsView(request, book_id):

    book = Book.objects.get(id=book_id)
    return render(request, 'user/userdetailsview.html', {'book': book})


def q(author__name__icontains):
    pass


def Search_Book(request):

    query=None
    books=None

    if 'g' in request.GET:

        query=request.GET.get('g')
        books=Book.objects.filter(Q(title__icontains=query) | q(author__name__icontains=query))
    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'user/usersearch.html',context)

def add_to_cart(request,book_id):
    book=Book.objects.get(id=book_id)

    if book.quantity>0:

        cart,created = Cart.objects.get_or_create(user=request.user)
        cart_item,item_created=CartItem.objects.get_or_create(cart=cart,book=book)

        if not item_created:

            cart_item.quantity+=1
            cart_item.save()
        return redirect('viewcart')

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items=Cart.cartitem_set.all()
    cart_item=CartItem.objects.all()
    total_price=sum(item.book.price + item.quantity for item in cart_items )
    total_items=cart_items.count()


    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    return render(request,'cart.html',context)


def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:

        cart_item.quantity+=1
        cart_item.save()
    return redirect('addtocart')

def decrease_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:

        cart_item.quantity-=1
        cart_item.save()
    return redirect('addtocart')

def remove_from_cart(request,item_id):

    try:
        cart_item=CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoseNotExist:
        pass

    return redirect('addtocart')



