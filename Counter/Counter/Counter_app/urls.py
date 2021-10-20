from django.urls import path    
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.index2),	   
    path('add2', views.index3),

]
