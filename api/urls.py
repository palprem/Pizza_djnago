from . import views
from django.urls import path

urlpatterns=[
    path('',views.AllAPI.as_view()),
    path('PizaAPI/',views.PizaAPI.as_view()),
    path('PizaAPI/<int:pk>',views.PizaAPI.as_view()),
    path('TopingAPI/',views.TopingAPI.as_view()),
    path('SizeAPI/',views.SizeAPI.as_view()),


]