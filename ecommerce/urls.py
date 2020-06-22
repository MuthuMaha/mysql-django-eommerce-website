from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("addcal",views.addcal,name="addcal"),
    path("result",views.result,name="result")
]