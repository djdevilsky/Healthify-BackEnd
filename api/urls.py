from django.urls import path
from api import views
urlpatterns = [
    path('doctors/', views.Doctors.as_view()),
]