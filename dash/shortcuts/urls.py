from django.urls import path

from . import views

urlpatterns = [
    path('<int:shortcut_id>/', views.redir, name='redir'),
    path('', views.index, name='index'),
]