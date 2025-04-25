from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book

# Step 3: User Authentication (Register, Login, Logout)
class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('book-list')
        return render(request, 'auth/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# Step 4: Book Listing and Details (CBV)
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'main/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'main/book_detail.html', {'book': book})


# Step 5: Cart Using Sessions
class AddToCartView(View):
    def get(self, request, book_id):
        cart = request.session.get('cart', {})
        cart[str(book_id)] = cart.get(str(book_id), 0) + 1
        request.session['cart'] = cart
        return redirect('view-cart')

class ViewCartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = Book.objects.filter(id__in=cart.keys())
        total_price = sum(book.price * cart[str(book.id)] for book in books)  # Calculate total price
        return render(request, 'main/cart.html', {'books': books, 'cart': cart, 'total_price': total_price})


class RemoveFromCartView(View):
    def get(self, request, book_id):
        cart = request.session.get('cart', {})
        cart.pop(str(book_id), None)
        request.session['cart'] = cart
        return redirect('view-cart')


# Step 6: Custom Admin Panel
class AdminBookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'admin/book_list.html', {'books': books})

class AdminAddBookView(View):
    def get(self, request):
        return render(request, 'admin/add_book.html')

    def post(self, request):
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            description=request.POST['description']
        )
        return redirect('admin-book-list')

class AdminEditBookView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'admin/edit_book.html', {'book': book})

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.stock = request.POST['stock']
        book.description = request.POST['description']
        book.save()
        return redirect('admin-book-list')

class AdminDeleteBookView(View):
    def get(self, request, pk):
        Book.objects.get(pk=pk).delete()
        return redirect('admin-book-list')
