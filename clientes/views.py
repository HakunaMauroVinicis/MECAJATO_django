from django.shortcuts import render
from django.http import response

# Create your views here.
def clientes(requeste):
    return httpResponse('estou em cliente')