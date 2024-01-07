from django.urls import path


from . import views


app_name = 'about'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('factory/', views.factory, name='factory'),
    path('information/', views.information, name='information'),
    path('', views.map, name='map'),
]
