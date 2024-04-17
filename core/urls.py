from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings


urlpatterns = [
    path("", include("booker.urls"), name="book_list"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
