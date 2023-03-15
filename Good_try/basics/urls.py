from django.urls import path

from . import views


app_name = 'basics'

urlpatterns = [
    path('', views.index, name='index'),
    path('basics/<int:data_id>', views.data_detail, name='data_detail'),
    path('basics/<int:data_id>/edit', views.data_edit, name='data_edit'),
    path('create/', views.data_create, name='data_create'),
]
