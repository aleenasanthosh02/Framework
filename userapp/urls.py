from django.urls import path
from . import views
from .views import increase_quantity

urlpatterns =[

    path("", views.listBook,name='Book List'),

    path('details/<int:book_id>/', views.detailsView,name='userdetails'),

    path('search-user/', views.Search_Book,name='usersearch'),

    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='addtocart'),
    path('view_cart/',views.view_cart,name='viewcart'),
    path('increase/<int:book_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:book_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove-from-cart,<int:book_id>/',views.remove_from_cart,name='remove_cart'),



]