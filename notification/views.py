from django.shortcuts import render, get_object_or_404, redirect
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from notification.utils import create_notification

def home(request):

    if request.user.is_authenticated:
        create_notification(request.user,"Welcom to OUr HOme Page")

    return render(request,'index.html')


@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-id')
    context = {
        'notifications':notifications,
    }
    return render(request, 'list.html', context)

@login_required
def mark_as_read(request,notification_id):
    notification = get_object_or_404(Notification,id=notification_id,user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('list')