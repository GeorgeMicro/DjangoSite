from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
	path('<int:pk>', views.PostView.as_view(), name='post')
]
