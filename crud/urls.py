from django.urls import path, include
from .views import addRecord, editRecord, deleteRecord

urlpatterns = [
    path('', addRecord, name='addRecord'),
    path('', editRecord, name='editRecord'),
    path('', deleteRecord, name='deleteRecord'),
]
