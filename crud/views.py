from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def addRecord(request):
    return HttpResponse('Function to add a record')

def editRecord(request):
    return HttpResponse('Function to edit a record')

def deleteRecord(request):
    return HttpResponse('Function to delete a record')