from django.urls import path
from .views import (
    BookListView, BookDetailView,
    AddToCartView, ViewCartView, RemoveFromCartView,
    RegisterView, LoginView, LogoutView,
    AdminBookListView, AdminAddBookView, AdminEditBookView, AdminDeleteBookView
)

urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Book Listing and Details (CBV)
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Cart Management (Session-based)
    path('cart/add/<int:book_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', ViewCartView.as_view(), name='view-cart'),
    path('cart/remove/<int:book_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),

    # Admin Panel URLs
    path('admin/books/', AdminBookListView.as_view(), name='admin-book-list'),
    path('admin/books/add/', AdminAddBookView.as_view(), name='admin-book-add'),
    path('admin/books/edit/<int:pk>/', AdminEditBookView.as_view(), name='admin-book-edit'),
    path('admin/books/delete/<int:pk>/', AdminDeleteBookView.as_view(), name='admin-book-delete'),
]
