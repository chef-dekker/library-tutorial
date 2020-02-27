from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: HttpResponse("Hello World", content_type="text/plain"))

]
