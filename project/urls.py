from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
]
