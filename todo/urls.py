from django.urls import path

from .views import index

app_name = 'todos'

urlpatterns = [
    path('', index, name='home'),
]


