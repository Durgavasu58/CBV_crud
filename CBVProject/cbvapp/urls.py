from django.urls import path
from .views import *

app_name='cbvapp'
urlpatterns = [
	path('',HomePage.as_view()),
	path('retrivedata/',StudentListView.as_view(),name='retrivedata'),
	path('studentform/',StudentFormView.as_view(),name='studentform'),
	path('update/<int:pk>/',StudentUpdateView.as_view(),name='update'),
	path('delete/<int:pk>/',StudentDeleteView.as_view(),name='delete')
]