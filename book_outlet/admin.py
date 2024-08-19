from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("title", "author", "rating")
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "rating")


admin.site.register(Book, BookAdmin)
