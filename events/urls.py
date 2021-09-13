from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/content', views.EventHtml.as_view(), name='event-html'),
    path('staffs/', views.StaffList.as_view(), name='staff-list'),
    path('staffs/<int:pk>/', views.StaffDetail.as_view(), name='staff-detail'),
    path('staffs/<int:pk>/content', views.StaffHtml.as_view(), name='staff-html'),
    path('foods/', views.FoodList.as_view(), name='food-list'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='food-list'),
    path('foods/<int:pk>/content/', views.FoodHtml.as_view(), name='food-html'),
    path('animals/', views.AnimalList.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalDetail.as_view(), name='animal-list'),
    path('animals/<int:pk>/content', views.AnimalHtml.as_view(), name='animal-html'),
    path('food-in-an-event/', views.FoodInAnEventList.as_view(), name='food-in-an-event-list'),
    path('food-in-an-event/<int:pk>/', views.FoodInAnEventDetail.as_view(), name='food-in-an-event-detail'),
    path('food-in-an-event/<int:pk>/', views.FoodInAnEventHtml.as_view(), name='food-in-an-event-html'),
    path('animal-in-an-event/', views.AnimalInAnEventList.as_view(), name='animal-in-an-event-list'),
    path('animal-in-an-event/<int:pk>/', views.AnimalInAnEventDetail.as_view(), name='animal-in-an-event-detail'),
    path('animal-in-an-event/<int:pk>/content', views.AnimalInAnEventHtml.as_view(), name='animal-in-an-event-html'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)