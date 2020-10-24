from django.urls import path
from .views import InputListView, InputDetailView, InputCreateView, InputUpdateView, InputDeleteView
from . import views

urlpatterns = [
    path('', InputListView.as_view(), name="home"),
    path('input/<int:pk>/', InputDetailView.as_view(), name="detail"),
    path('input/<int:pk>/update/', InputUpdateView.as_view(), name="update"),
    path('input/<int:pk>/delete/', InputDeleteView.as_view(), name="delete"),
    path('input/new/', InputCreateView.as_view(), name="create"),
    path('about/', views.about, name="about"),

]
