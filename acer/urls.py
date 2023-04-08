from django.urls import path
from acer.views import Show_view, Add

urlpatterns =[
    path("",Show_view),
    path("", Add)
]