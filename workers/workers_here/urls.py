from django.urls import path
from .views import *

urlpatterns = [
    path('<int:worker_id>/', WorkerDetailed.as_view(), name = 'worker_detailed'),
    path('all/', WorkerFull.as_view(), name = 'all_workers'),
    path('search/', WorkerSearch.as_view(), name = 'search'),
    path('all/sorted/', WorkerSortedName.as_view(), name = 'all_workers_sorted'),
    path('login/', register_user, name='register_user'),
    path('register/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]