from django.urls import path
from . import views

urlpatterns = [

   path('', views.index,name='home'),
   path('weather', views.index2,name='search'),
   path('info', views.about,name='info'),
   path('map',views.map,name='map')
]
