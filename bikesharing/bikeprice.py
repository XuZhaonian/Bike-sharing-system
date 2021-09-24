from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import BikeRoute
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class bikeprice:
    def showchoseplot(request):
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
            palette = ["LightSeaGreen", "MediumPurple", "Yellow", "Red", "Pink", "Brown", "Orange", "RoyalBlue"]
            chose_price_list = []
            for x in range((int(end_day) - int(start_day)+1)):
                chose_price_list.append([0, 0, 0, 0, 0, 0, 0, 0])
            bike_route = BikeRoute.objects.all()
            for i in range(len(bike_route)):
                if bike_route[i].route_starttime.day >= int(start_day) and bike_route[i].route_starttime.day <= int(end_day):
                    chose_price_list[bike_route[i].route_starttime.day - int(start_day)][
                        bike_route[i].route_starttime.hour // 3] += bike_route[i].route_price
            fig = make_subplots(rows=1, cols=2)
            fig.add_bar(y=chose_price_list[0],
                        marker=dict(color=palette[0]),
                        name=start_day, row=1, col=1)
            for i in range((int(end_day) - int(start_day))):
                fig.add_scatter(y=chose_price_list[i + 1], mode="markers",
                                marker=dict(size=20, color=palette[i + 1]),
                                name=str(int(start_day)+i+1), row=1, col=1)
            fig.update_traces(marker=dict(color="RoyalBlue"), col=2)
            fig.write_html("templates/bikeprice.html")
            time_period = [int(start_day),int(end_day)]
            return render(request, '../templates/manager_bikeprice_plot.html', {'time_period':time_period})

    def showinitialplot(request):
        palette = ["LightSeaGreen", "MediumPurple", "Yellow", "Red", "Pink", "Brown", "Orange", "RoyalBlue"]
        initial_price_list = []
        for x in range(6):
            initial_price_list.append([0, 0, 0, 0, 0, 0, 0, 0])
        bike_route = BikeRoute.objects.all()
        for i in range(len(bike_route)):
            if bike_route[i].route_starttime.day > 22:
                initial_price_list[bike_route[i].route_starttime.day-23][bike_route[i].route_starttime.hour//3] += bike_route[i].route_price

        fig = make_subplots(rows=1, cols=2)
        fig.add_bar(y=initial_price_list[0],
                    marker=dict(color=palette[0]),
                    name=str(23), row=1, col=1)
        for i in range(5):
            fig.add_scatter(y=initial_price_list[i+1], mode="markers",
                            marker=dict(size=20, color=palette[i+1]),
                            name=str(i+24), row=1, col=1)

        fig.update_traces(marker=dict(color="RoyalBlue"), col=2)
        fig.write_html("templates/bikeprice.html")
        time_period = [23,28]
        return render(request, '../templates/manager_bikeprice_plot.html', {'time_period':time_period})
