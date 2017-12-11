from django import forms
from django.forms import ModelForm
from .models import *


class TerminalFrom(forms.Form):
    passengertraffic = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    radarrange = models.BigIntegerField(blank=True, null=True)
    callsign = models.CharField(db_column='callsign', max_length=4, blank=True, null=True)


class RunwayForm(ModelForm):
    class Meta:
        model = Runway
        fields = ['runway_id', 'length', 'weightallowed', 'terminal']


class PlaneForm(ModelForm):
    class Meta:
        model = Plane
        fields = ['plane_id', 'seats', 'fuelweight', 'wingspan']


class GatesForm(ModelForm):
    class Meta:
        model = Gates
        fields = ['gates_id', 'throughput', 'type', 'terminal']


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id', 'passengers', 'plane', 'timeofarrival', 'gates', 'type', 'runway', 'timeofdeparture']


class CargodepotFrom(ModelForm):
    class Meta:
        model = Cargodepot
        fields = ['cargo_id', 'height', 'volume', 'numberofloaders', 'terminal']


class TerminalzForm(ModelForm):
    class Meta:
        model = Terminal
        fields = ['terminal_id', 'passengertraffic', 'type', 'city', 'radarrange', 'callsign']