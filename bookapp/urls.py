from django.urls import path
from . import views
from .views import createBook

urlpatterns =[
    path("create-book",views.createBook,name='createbook'),

    path('', views.listBook,name='booklist'),

    path('author', views.Create_Author,name='author'),

    path('detailsview/<int:book_id>/', views.detailsView,name='details'),

    path('updateview/<int:book_id>/', views.updateBook,name='update'),

    path('deleteview/<int:book_id>/', views.deleteView,name='delete'),

    path('index', views.index)


]