from django.urls import path
from . import views

urlpatterns = [
    path('generate-routine/', views.create_routine_view, name='generate_routine'),
]