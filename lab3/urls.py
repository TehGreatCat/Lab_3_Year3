from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('Terminal/', Terminal_show, name="Terminal"),
    path('Terminal_add/', Terminal_add, name="Terminal_add"),
    path('Terminal/Terminal_add/<terminal_id>/', Terminal_update, name="Terminal_update"),
    path('Runway/', Runway_show, name="Runway"),
    path('Runway_add/', Runway_add, name="Runway_add"),
    path('Terminal/Runway_add/<runway_id>/', Runway_update, name="Runway_update"),
    path('Plane/', Plane_show, name="Plane"),
    path('Plane_add/', Plane_add, name="Plane_add"),
    path('Terminal/Plane_add/<plane_id>/', Plane_update, name="Plane_update"),
    path('Gates/', Gates_show, name="Gates"),
    path('Gate_add/', Gates_add, name="Gates_add"),
    path('Terminal/Gate_add/<gates_id>/', Gates_update, name="Gates_update"),
    path('Flight/', Flight_show, name="Flight"),
    path('Flight_add/', Flight_add, name="Flight_add"),
    path('Terminal/Flight_add/<flight_id>/', Flight_update, name="Flight_update"),
    path('Cargodepot/', Cargodepot_show, name="Cargodepot"),
    path('Cargodepot_add/', Cargodepot_add, name="Cargodepot_add"),
    path('Terminal/Cargodepot_add/<cargo_id>/', Cargodepot_update, name="Cargodepot_update")
]
