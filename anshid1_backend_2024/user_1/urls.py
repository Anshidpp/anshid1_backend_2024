from django.urls import path
from . import views

urlpatterns=[
    path('register',views.registerform,name='registerform'),
    path('csrf',views.get_csrf_token,name='csrftoken'),
    path('login',views.Login,name='login'),
    path('logout',views.logouts,name='logout'),
    path('display',views.displaydetailes,name='displaydetailes'),
    path('update',views.updatedetails,name='updatedetails'),
    path('delete',views.deletedetails,name='deletedetails'),
    path('booking',views.bookingdetails,name='bookingdetails'),
    path('search/<str:name>',views.searchdetails,name='searchdetails')
]