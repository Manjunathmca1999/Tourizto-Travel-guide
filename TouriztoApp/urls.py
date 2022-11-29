from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AboutUs/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('ChatWithUs/', views.chatbot, name='chatbot'),
    path('Location/', views.location, name='location'),
    path('Terms/', views.terms, name='terms'),
    path('Results/', views.search, name='search'),
    path('AddItenary/', views.new_itenary, name='new_itenary'),
    path('Destination/<str:id>/', views.view_itenary, name='view_itenary'),
    path('Destination/<str:id>/like/', views.like, name='like'),
    path('Destination/<str:id>/update/', views.update_itenary, name='update_itenary'),
    path('Destination/<str:id>/remove/', views.delete_itenary, name='delete_itenary'),
]
