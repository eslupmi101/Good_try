from django.views.generic import TemplateView

from django.urls import path

from . import views


app_name = 'basics'

urlpatterns = [
    path('', views.index, name='index'),
    path('data/<int:data_id>/', views.profile_rent, name='profile_rent'),
    path('basics/<int:data_id>/edit', views.data_edit, name='data_edit'),
    path('create/', views.data_create, name='data_create'),
    path(
        'application_rent/',
        TemplateView.as_view(template_name="basics/application_rent.html"),
        name='application_rent'
    ),
    path(
        'user_booking/<str:username>/',
        views.user_booking,
        name='user_booking'
    ),
    path(
        'accept_booking/',
        views.accept_booking,
        name='accept_booking'
    ),
    path('booking_accomodation/<int:accom_id>/',
         views.booking_accomodation,
         name='booking_accomodation'),
]
