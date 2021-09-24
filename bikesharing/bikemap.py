import pandas as pd
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from bikesharing.models import BikeAttribute, BikeState
from bikesharing import checkuser
import numpy


class bikemap:
    def getbikepos(request):
        x = checkuser.userLog.teststilllogin(request)
        if x == 1:
            return redirect("/login/")
        elif x == 0:
            file = open('bikeposition.csv', 'w')
            csv_writer = csv.writer(file)
            csv_writer.writerow(["No.", "posx", "posy"])
            bike_state = BikeState.objects.get(state_id=1)
            bike_state_list = list(BikeAttribute.objects.filter(bike_state=bike_state))
            bike_list = []
            for i in bike_state_list:
                # bike_list.append(list(BikeAttribute.objects.get(bike_state=bike_state_list[i])))
                l = [i.bike_id, i.bike_stationx, i.bike_stationy]
                bike_list.append(l)
            csv_writer.writerows(bike_list)
            file.close()
            # bike_csv = pd.read_csv("bikeposition.csv")
            # drawmap = px.scatter_mapbox(bike_csv, lat="posy", lon="posx", color="num",
            #                             color_continuous_scale=px.colors.cyclical.IceFire,  zoom=10, height=500)
            # drawmap.update_layout(mapbox_style="open-street-map")
            # drawmap.update_layout(margin={"r": 100, "t": 150, "l": 100, "b": 0})
            # drawmap.write_html("templates/bikemap.html")
            # print(bike_list)
            # return render(request, "index_04.html", {'bikeshow': bike_state_list})
            return redirect("/makemap/")
            # return HttpResponse("already!")
        else:
            return HttpResponse("Something is going wrong!")


    def makemap(request):
        # cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
        bike_csv = pd.read_csv("D:/python/pythonProject/bbs/" + "bikeposition.csv")

        # fig = px.scatter_mapbox(bike_csv, lat="lat", lon="lon", hover_name="City", hover_data=["State"],
        #                         color_discrete_sequence=["fuchsia"], zoom=10, height=500)
        fig = px.scatter_mapbox(bike_csv, lat="posy", lon="posx", color="No.",
                                    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, height=500)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 50, "t": 50, "l": 50, "b": 0})
        fig.write_html("templates/bikemap.html")
        # fig.write_html("testmap.html")
        return redirect("/manager/bikemap/")
        # return render(request, '../templates/index_manager.html')

    def showmap(request):
        return render(request, '../templates/index_manager.html')