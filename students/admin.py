from django.contrib import admin
from students.models import Book, Student, BorrowedBook
from django.contrib.admin import AdminSite
from .admin_models import AdminUser

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image_display']  # Add image_display
    search_fields = ['title', 'author']

    # Method to display image thumbnail in the admin
    def image_display(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "No Image"
    image_display.short_description = 'Cover'
    image_display.allow_tags = True

class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'student_id']
    search_fields = ['student_id']

class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'student', 'borrowed_at', 'return_by']

class LibraryAdminSite(AdminSite):
    site_header = "Library Administration"
    
    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff
    
admin.site.register(Book, BookAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(BorrowedBook, BorrowedBookAdmin)
admin.site.register(AdminUser)
