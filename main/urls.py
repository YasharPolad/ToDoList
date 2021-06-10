from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('add/', add, name = 'add'),
    path('delete/<int:id>', delete, name = 'delete'),
    path('share/<int:id>', share, name = 'share'),
    path('view/<int:id>', view, name = 'view'),
]