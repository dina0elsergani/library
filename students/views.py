from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Book
from django.contrib.auth.decorators import login_required
from .models import BorrowedBook,Student
import datetime
from .forms import ProfileUpdateForm, UserRegisterForm
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False) 
                user.set_password(form.cleaned_data['password'])  
                user.save()  
                login(request, user)
                return redirect('students:book_list')
            except IntegrityError:
                form.add_error('student_id', 'This student ID is already taken.')
    else:
        form = UserRegisterForm()
    return render(request, 'students/html/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:
            user = Student.objects.get(username=username)  
            if check_password(password, user.password):
                login(request, user)
                return redirect('students:book_list')  
            else:
                return render(request, 'students/html/login.html', {'error': 'Invalid username or password.'})
        except Student.DoesNotExist:
            return render(request, 'students/html/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'students/html/login.html')  
def logout_view(request):
    logout(request)
    return redirect('students:login')

def book_list(request):
    books = Book.objects.all()
    borrowed_books = BorrowedBook.objects.filter(student=request.user)
    borrowed_books_ids = [borrowed.book.id for borrowed in borrowed_books]
    return render(request, 'students/html/book_list.html', {'books': books, 'borrowed_books_ids': borrowed_books_ids})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)

    already_borrowed = BorrowedBook.objects.filter(student=request.user, book=book).exists()

    if already_borrowed:
        message = "You've already borrowed this book!"
        books = Book.objects.all()
        return render(request, 'students/html/book_list.html', {'books': books, 'error_message': message})
    else:
        borrow = BorrowedBook(student=request.user, book=book, return_by=datetime.datetime.now() + datetime.timedelta(days=7))
        borrow.save()
        return redirect('students:dashboard')

@login_required
def dashboard(request):
    borrowed_books = BorrowedBook.objects.filter(student=request.user)
    return render(request, 'students/html/dashboard.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request, borrow_id):
    borrow = BorrowedBook.objects.get(id=borrow_id)
    borrow.delete()
    return redirect('students:dashboard')

@login_required
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'students/html/book_details.html', {'book': book})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('students:book_list')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'students/html/profile.html', {'form': form})