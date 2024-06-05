from django.contrib import admin
from django.urls import path, include
from notification import urls as notification_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(notification_urls)),
]
