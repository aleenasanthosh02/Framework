from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect
from .forms import AuthorForm,BookForms
from .models import Book,Author
# Create your views here.
from django.db.models import Q
from.models import Book


# def createBook(request):
#
#     books = Book.objects.all()
#
#     if request.method=='POST':
#
#         title=request.POST.get('title')
#         Price=request.POST.get('Price')
#
#         book=Book(title=title,Price=Price)
#
#         book.save()
#
#     return render(request,'book.html',{'books':books})


def listBook(request):

    books=Book.objects.all()
    paginator=Paginator(books, 4)
    page_number = request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/listbook.html',{'books':books,'page':page})

def detailsView(request, book_id):

    book = Book.objects.get(id=book_id)
    return render(request, 'admin/detailsview.html', {'book': book})

def updateBook(request, book_id):

    book= Book.objects.get(id=book_id)

    if request.method=='POST':
        form = BookForms(request.POST,instance=book)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form=BookForms(instance=book)

    return render(request,'admin/updateview.html', {'form':form})


def deleteView(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method=="POST":

        book.delete()

        return redirect("/")

    return render(request, 'admin/deleteview.html', {'book':book} )


def index(request):
    return render(request,'admin/base.html')



def createBook(request):
    books=Book.objects.all()

    if request.method=="POST":
        form=BookForms(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = BookForms()

    return render(request,'admin/book.html',{'form':form,'books':books})

def Create_Author(request):
    author=Author.objects.all()
    if request.method=="POST":

        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = AuthorForm()

    return render(request, 'admin/book.html', {'form': form})




