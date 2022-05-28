from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('<int:worker_id>/', WorkerDetailed.as_view(), name = 'worker_detailed'),
    path('all/', WorkerFull.as_view(), name = 'all_workers'),
    path('search/', WorkerSearch.as_view(), name = 'search'),
    path('all/sorted/', WorkerSortedName.as_view(), name = 'all_workers_sorted'),
    path('login/', register_user, name='register_user'),
    path('register/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('<int:worker_id>/delete/', delete_user, name='delete_worker'),
    path('<int:worker_id>/edit/', edit_worker, name='edit'),
    path('all/add_worker/', WorkerAddition.as_view(), name='addition'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)