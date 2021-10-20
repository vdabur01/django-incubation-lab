from django.shortcuts import render
from django.http import HttpResponse


def fetchAllEmployees(request):
    return HttpResponse('Employee records.')
