from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import *
from .forms import *
import re
import psycopg2
from prettytable import PrettyTable
# Create your views here.


def index(request):
    return render(request, "index.html")


def Terminal_show(request):
    terminals = Terminal.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            terminals = terminals.\
                filter(Q(type__contains=query) | Q(callsign__contains=query) | Q(city__contains=query))
        else:
            terminals = terminals.filter(
                Q(passengertraffic__exact=query) |
                Q(radarrange__exact=query) |
                Q(terminal_id=query)
            ).distinct()
    ctx = {'terminals': terminals}
    return render(request, 'Terminal.html', ctx)


def Terminal_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Terminal")
    form = TerminalzForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Terminal/')
    return render(request, 'Terminal_add.html', {'form': form})


def Terminal_update(request, terminal_id):
    instanse = get_object_or_404(Terminal, pk=terminal_id)
    terminal = Terminal.objects.get(pk=terminal_id)
    form = TerminalzForm(instance=instanse)
    if request.method == "POST":
        form = TerminalzForm(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            terminal.delete()
            return redirect("Terminal")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Terminal/')
    context = {
        "form": form,
        "title": "Terminal",
        "instance": instanse,
    }
    return render(request, 'Terminal_add.html', context)


def Runway_show(request):
    runways = Runway.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            runways = runways.filter(
                Q(length__exact=query) |
                Q(weightallowed__exact=query) |
                Q(terminal=query)
            ).distinct()
        except ValueError as e:
            print(e)
    ctx = {'runways': runways}
    return render(request, 'Runway.html', ctx)


def Runway_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Runway")
    form = RunwayForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Runway/')
    return render(request, 'Runway_add.html', {'form': form})


def Runway_update(request, runway_id):
    instanse = get_object_or_404(Runway, pk=runway_id)
    runway = Runway.objects.get(pk=runway_id)
    form = RunwayForm(instance=instanse)
    if request.method == "POST":
        form = RunwayForm(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            runway.delete()
            return redirect("Runway")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Runway/')
    context = {
        "form": form,
        "title": "Runway",
        "instance": instanse,
    }
    return render(request, 'Runway_add.html', context)


def Plane_show(request):
    planes = Plane.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            planes = planes.\
                filter(Q(plane_id__contains=query))
        else:
            planes = planes.filter(
                Q(seats__exact=query) |
                Q(fuelweight__exact=query) |
                Q(wingspan__exact=query)
            ).distinct()
    ctx = {'planes': planes}
    return render(request, 'Plane.html', ctx)


def Plane_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Plane")
    form = PlaneForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Plane/')
    return render(request, 'Plane_add.html', {'form': form})


def Plane_update(request, plane_id):
    instanse = get_object_or_404(Plane, pk=plane_id)
    plane = Plane.objects.get(pk=plane_id)
    form = PlaneForm(instance=instanse)
    if request.method == "POST":
        form = PlaneForm(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            plane.delete()
            return redirect("Plane")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Plane/')
    context = {
        "form": form,
        "title": "Plane",
        "instance": instanse,
    }
    return render(request, 'Plane_add.html', context)


def Gates_show(request):
    gates = Gates.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            gates = gates.\
                filter(Q(type__contains=query))
        else:
            gates = gates.filter(
                Q(throughput__exact=query) |
                Q(gates_id__exact=query) |
                Q(terminal=query)
            ).distinct()
    ctx = {'gates': gates}
    return render(request, 'Gates.html', ctx)


def Gates_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Gate")
    form = GatesForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Gate/')
    return render(request, 'Gates_add.html', {'form': form})


def Gates_update(request, gates_id):
    instanse = get_object_or_404(Gates, pk=gates_id)
    gates = Gates.objects.get(pk=gates_id)
    form = GatesForm(instance=instanse)
    if request.method == "POST":
        form = GatesForm(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            gates.delete()
            return redirect("Gates")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Gates/')
    context = {
        "form": form,
        "title": "Gates",
        "instance": instanse,
    }
    return render(request, 'Gates_add.html', context)


def Flight_show(request):
    flights = Flight.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            flights = flights.filter(Q(plane__contains=query) | Q(type__contains=query) |
                                     Q(timeofarrival__exact=query) | Q(timeofdeparture__exact=query))
        else:
            flights = flights.filter(
                Q(flight_id__exact=query) |
                Q(passengers__exact=query) |
                Q(gates__exact=query) |
                Q(runway__exact=query)
            ).distinct()
    ctx = {'flights': flights}
    return render(request, 'Flight.html', ctx)


def Flight_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Flight")
    form = FlightForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Flight/')
    return render(request, 'Flight_add.html', {'form': form})


def Flight_update(request, flight_id):
    instanse = get_object_or_404(Flight, pk=flight_id)
    flight = Flight.objects.get(pk=flight_id)
    form = FlightForm(instance=instanse)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            flight.delete()
            return redirect("Flight")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Flight/')
    context = {
        "form": form,
        "title": "Flight",
        "instance": instanse,
    }
    return render(request, 'Flight_add.html', context)


def Cargodepot_show(request):
    cargodepots = Cargodepot.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            cargodepots = cargodepots.filter(
                Q(cargo_id__exact=query) |
                Q(height__exact=query) |
                Q(volume__exact=query) |
                Q(numberofloaders__exact=query) |
                Q(terminal=query)
            ).distinct()
        except ValueError as e:
            print(e)
    ctx = {'Cargodepots': cargodepots}
    return render(request, 'Cargodepot.html', ctx)


def Cargodepot_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("Cargodepot")
    form = CargodepotFrom(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal1/Cargodepot/')
    return render(request, 'Cargodepot_add.html', {'form': form})


def Cargodepot_update(request, cargo_id):
    instanse = get_object_or_404(Cargodepot, pk=cargo_id)
    cargodepot = Cargodepot.objects.get(pk=cargo_id)
    form = CargodepotFrom(instance=instanse)
    if request.method == "POST":
        form = CargodepotFrom(request.POST, instance=instanse)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            cargodepot.delete()
            return redirect("Cargodepot")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal1/Cargodepot/')
    context = {
        "form": form,
        "title": "Cargodepot",
        "instance": instanse,
    }
    return render(request, 'Cargodepot_add.html', context)
