from django.urls import path
from notification.views import notification_list, mark_as_read, home

urlpatterns = [
    path('', home, name="home"),
    path('view-all-notifcations/', notification_list, name='list'),    
    path("mark_as_read/<int:notification_id>/", mark_as_read, name='mark_as_read')
]
