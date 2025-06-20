from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """Index view function for lookup application.

    params:
    -------
    request: HTTP request data

    returns:
    --------
    django.http.HttpResponse object
    """

    return HttpResponse("Hello CO Tax Lookup!")
