from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('staffs/', views.StaffList.as_view()),
    path('staffs/<int:pk>/', views.StaffDetail.as_view()),
    path('foods/', views.FoodList.as_view()),
    path('foods/<int:pk>/', views.FoodDetail.as_view()),
    path('animals/', views.AnimalList.as_view()),
    path('animals/<int:pk>/', views.AnimalDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)