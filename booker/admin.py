from django.contrib import admin

from booker.models import Book, Author, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date")
    list_filter = ("genre", "publish_date")
    search_fields = ("title", "author__name")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
