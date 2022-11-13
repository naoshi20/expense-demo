from django.urls import path

from .views import IndexView, AddView

app_name = 'appName'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('add/', AddView.as_view(), name="add"),
]