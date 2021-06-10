from .views import symptoms_return, predict, get_description
from django.urls import path

urlpatterns = [
    path("symptoms-return/",symptoms_return,name="symptoms_return"),
    path("predict/",predict,name="predict"),
    path("get-description/<str:id_field>/",get_description,name="get_description"),
]
