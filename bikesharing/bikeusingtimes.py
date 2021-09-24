from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import BikeAttribute,BikeRoute
import plotly.graph_objects as go
import pandas as pd

class bikeusingtimes:
    def showinitialplot(request):
        bike_route = BikeRoute.objects.all()
        bike_initial_times = []
        times_23 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        times_24 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        times_25 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        times_26 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        times_27 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        times_28 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(len(bike_route)):
            if bike_route[i].route_starttime.day == 23:
                times_23[bike_route[i].route_starttime.hour] += 1
            elif bike_route[i].route_starttime.day == 24:
                times_24[bike_route[i].route_starttime.hour] += 1
            elif bike_route[i].route_starttime.day == 25:
                times_25[bike_route[i].route_starttime.hour] += 1
            elif bike_route[i].route_starttime.day == 26:
                times_26[bike_route[i].route_starttime.hour] += 1
            elif bike_route[i].route_starttime.day == 27:
                times_27[bike_route[i].route_starttime.hour] += 1
            elif bike_route[i].route_starttime.day == 28:
                times_28[bike_route[i].route_starttime.hour] += 1
        bike_initial_times.append(times_23)
        bike_initial_times.append(times_24)
        bike_initial_times.append(times_25)
        bike_initial_times.append(times_26)
        bike_initial_times.append(times_27)
        bike_initial_times.append(times_28)
        time_period = [23,28]
        fig = go.Figure(
            # data=go.Surface(z=z_data.values),
            data=go.Surface(z=bike_initial_times),
            layout=go.Layout(
                title="Bike Used Times",
                width=800,
                height=800,
            ))
        fig.update_layout(template="none", title="Bike Used Times")
        fig.write_html("templates/bikeusedtimes.html")
        return render(request, '../templates/manager_bikeusedtimes_plot.html', {'time_period':time_period})

    def showchoseplot(request):
        start_day = 23
        end_day = 28
        if request.method == "POST":
            start_time = request.POST.get("start_time")
            start_year = start_time[0:4]
            start_month = start_time[5:7]
            start_day = start_time[8:10]
            start_hour = start_time[11:13]
            start_minute = start_time[14:]
            end_time  = request.POST.get("end_time")
            end_year = end_time[0:4]
            end_month = end_time[5:7]
            end_day = end_time[8:10]
            end_hour = end_time[11:13]
            end_minute = end_time[14:]
            lenth = int(end_day) - int(start_day)
            bike_chose_times = []
            for i in range(lenth):
                bike_chose_times.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            bike_route = BikeRoute.objects.all()
            for a in range(len(bike_route)):
                for b in range(lenth):
                    if bike_route[a].route_starttime.day == (int(start_day)+b):
                        bike_chose_times[b][bike_route[a].route_starttime.hour] += 1
            fig = go.Figure(
                # data=go.Surface(z=z_data.values),
                data=go.Surface(z=bike_chose_times),
                layout=go.Layout(
                    title="Bike Used Times",
                    width=800,
                    height=800,
                ))
            time_period = [int(start_day), int(end_day)]
            fig.update_layout(template="none", title="Bike Used Times")
            fig.write_html("templates/bikeusedtimes.html")
            return render(request, '../templates/manager_bikeusedtimes_plot.html', {'time_period':time_period})
