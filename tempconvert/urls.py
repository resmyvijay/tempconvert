from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),  #the path for our index view
	path(r'submit', views.convert),
	path(r'submit', views.convert)
]

