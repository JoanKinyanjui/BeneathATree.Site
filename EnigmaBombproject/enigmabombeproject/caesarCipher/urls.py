from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('sentmessage/' ,views.sentmessage, name='sentmessage'),
    path('decipher/', views.decipher, name='decipher')
    
]
