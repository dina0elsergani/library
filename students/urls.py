from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'students'

urlpatterns = [
    path('',TemplateView.as_view(template_name='students/html/base.html')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('book_list/', views.book_list, name='book_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('book_details/<int:book_id>/', views.book_details, name='book_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
    path('profile/', views.profile, name='profile'),
]

