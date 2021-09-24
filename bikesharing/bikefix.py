from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import BikeAttribute,BikeFixed
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import csv

class bikefix:
    # def showbikefix(request):
        # starttime =
        # return redirect()


    def getfixdata(request):
        initial_fix_list = BikeFixed.objects.all()
        fix_count_28 = [0, 0, 0, 0, 0, 0, 0, 0]
        fix_count_6_day = [0,0,0,0,0,0]
        fix_count_chose = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(initial_fix_list)):
            initial_fix = BikeFixed.objects.get(fixed_id=(i + 1))
            if initial_fix.fixed_time.day == 28:
                fix_count_6_day[5] += 1
                if initial_fix.fixed_time.hour >= 0 and initial_fix.fixed_time.hour < 3:
                    fix_count_28[0] += 1
                elif initial_fix.fixed_time.hour >= 3 and initial_fix.fixed_time.hour < 6:
                    fix_count_28[1] += 1
                elif initial_fix.fixed_time.hour >= 6 and initial_fix.fixed_time.hour < 9:
                    fix_count_28[2] += 1
                elif initial_fix.fixed_time.hour >= 9 and initial_fix.fixed_time.hour < 12:
                    fix_count_28[3] += 1
                elif initial_fix.fixed_time.hour >= 12 and initial_fix.fixed_time.hour < 15:
                    fix_count_28[4] += 1
                elif initial_fix.fixed_time.hour >= 15 and initial_fix.fixed_time.hour < 18:
                    fix_count_28[5] += 1
                elif initial_fix.fixed_time.hour >= 18 and initial_fix.fixed_time.hour < 21:
                    fix_count_28[6] += 1
                else:
                    fix_count_28[7] += 1
            elif initial_fix.fixed_time.day == 27:
                fix_count_6_day[4] += 1
            elif initial_fix.fixed_time.day == 26:
                fix_count_6_day[3] += 1
            elif initial_fix.fixed_time.day == 25:
                fix_count_6_day[2] += 1
            elif initial_fix.fixed_time.day == 24:
                fix_count_6_day[1] += 1
            elif initial_fix.fixed_time.day == 23:
                fix_count_6_day[0] += 1
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
            if start_day == end_day:
                for i in range(len(initial_fix_list)):
                    initial_fix = BikeFixed.objects.get(fixed_id=(i + 1))
                    if initial_fix.fixed_time.day == int(start_day):
                        if initial_fix.fixed_time.hour >= 0 and initial_fix.fixed_time.hour < 3:
                            fix_count_chose[0] += 1
                        elif initial_fix.fixed_time.hour >= 3 and initial_fix.fixed_time.hour < 6:
                            fix_count_chose[1] += 1
                        elif initial_fix.fixed_time.hour >= 6 and initial_fix.fixed_time.hour < 9:
                            fix_count_chose[2] += 1
                        elif initial_fix.fixed_time.hour >= 9 and initial_fix.fixed_time.hour < 12:
                            fix_count_chose[3] += 1
                        elif initial_fix.fixed_time.hour >= 12 and initial_fix.fixed_time.hour < 15:
                            fix_count_chose[4] += 1
                        elif initial_fix.fixed_time.hour >= 15 and initial_fix.fixed_time.hour < 18:
                            fix_count_chose[5] += 1
                        elif initial_fix.fixed_time.hour >= 18 and initial_fix.fixed_time.hour < 21:
                            fix_count_chose[6] += 1
                        else:
                            fix_count_chose[7] += 1
                hours = ["0-3", "3-6", "6-9", "9-12", "12-15", "15-18", "18-21", "21-24"]
                fig = px.line(x=hours, y=fix_count_28, color=px.Constant("28th"),
                              labels=dict(x="Periods of time", y="Amount of fixed", color="Day"))
                fig.add_bar(x=hours, y=fix_count_chose, name=str(start_day))
                fig.write_html("templates/bikefix.html")
            elif (int(end_day) - int(start_day)) < 6:
                lenth = int(end_day) - int(start_day)
                for i in range(len(initial_fix_list)):
                    initial_fix = BikeFixed.objects.get(fixed_id=(i + 1))
                    for x in range(lenth):
                        if initial_fix.fixed_time.day == (int(start_day)+x):
                            fix_count_chose[x] += 1
                days = ["first_day", "second_day", "third_day", "forth_day", "fifth_day", "sixth_day"]
                fig = px.line(x=days, y=fix_count_6_day, color=px.Constant("23-28"),
                              labels=dict(x="Periods of time", y="Amount of fixed", color="Day"))
                fig.add_bar(x=days, y=fix_count_chose, name=(str(start_day)+"-"+str(end_day)))
                fig.write_html("templates/bikefix.html")
        return render(request, '../templates/manager_bikefix_plot.html')

    # def setinitialdata(request):
    #     initial_fix_list = BikeFixed.objects.all()
    #     set_initial_fix = []
    #     for i in range(len(initial_fix_list)):
    #         initial_fix = BikeFixed.objects.get(fixed_id=(i+1))
    #         if initial_fix.fixed_time.day == 24:
    #             set_initial_fix.append(list([initial_fix.fixed_id, initial_fix.fixed_time, initial_fix.fixed_bike_id]))
    #     file = open('bikeinitialfix.csv', 'w')
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerow(["fixed_id", "fixed_time", "bike_id"])
    #     return HttpResponse(set_initial_fix[0])

    def showinitialplot(request):
        # fig = go.Figure(
        #     data=[go.Bar(y=np.arange(5, 11), x=np.arange(2, 8))],
        #     layout_title_text="The Figure of FIX DATA on 24/2/2021"
        # )
        initial_fix_list = BikeFixed.objects.all()
        set_initial_fix = []
        fix_count = [0,0,0,0,0,0,0,0]
        fix_count_28 = [0,0,0,0,0,0,0,0]
        for i in range(len(initial_fix_list)):
            initial_fix = BikeFixed.objects.get(fixed_id=(i + 1))
            if initial_fix.fixed_time.day == 24:
                if initial_fix.fixed_time.hour >= 0 and initial_fix.fixed_time.hour < 3:
                    fix_count[0] += 1
                    # fix_count_28[0] += 1
                elif initial_fix.fixed_time.hour >= 3 and initial_fix.fixed_time.hour < 6:
                    fix_count[1] += 1
                    # fix_count_28[1] += 1
                elif initial_fix.fixed_time.hour >= 6 and initial_fix.fixed_time.hour < 9:
                    fix_count[2] += 1
                    # fix_count_28[2] += 1
                elif initial_fix.fixed_time.hour >= 9 and initial_fix.fixed_time.hour < 12:
                    fix_count[3] += 1
                    # fix_count_28[3] += 1
                elif initial_fix.fixed_time.hour >= 12 and initial_fix.fixed_time.hour < 15:
                    fix_count[4] += 1
                    # fix_count_28[4] += 1
                elif initial_fix.fixed_time.hour >= 15 and initial_fix.fixed_time.hour < 18:
                    fix_count[5] += 1
                    # fix_count_28[5] += 1
                elif initial_fix.fixed_time.hour >= 18 and initial_fix.fixed_time.hour < 21:
                    fix_count[6] += 1
                    # fix_count_28[6] += 1
                else:
                    fix_count[7] += 1
                    # fix_count_28[7] += 1
                # set_initial_fix.append(list([initial_fix.fixed_id, initial_fix.fixed_time, initial_fix.fixed_bike_id]))
            elif initial_fix.fixed_time.day == 28:
                if initial_fix.fixed_time.hour >= 0 and initial_fix.fixed_time.hour < 3:
                    fix_count_28[0] += 1
                elif initial_fix.fixed_time.hour >= 3 and initial_fix.fixed_time.hour < 6:
                    fix_count_28[1] += 1
                elif initial_fix.fixed_time.hour >= 6 and initial_fix.fixed_time.hour < 9:
                    fix_count_28[2] += 1
                elif initial_fix.fixed_time.hour >= 9 and initial_fix.fixed_time.hour < 12:
                    fix_count_28[3] += 1
                elif initial_fix.fixed_time.hour >= 12 and initial_fix.fixed_time.hour < 15:
                    fix_count_28[4] += 1
                elif initial_fix.fixed_time.hour >= 15 and initial_fix.fixed_time.hour < 18:
                    fix_count_28[5] += 1
                elif initial_fix.fixed_time.hour >= 18 and initial_fix.fixed_time.hour < 21:
                    fix_count_28[6] += 1
                else:
                    fix_count_28[7] += 1
        hours = ["0-3", "3-6", "6-9", "9-12", "12-15", "15-18", "18-21", "21-24"]
        fig = px.line(x=hours, y=fix_count_28, color=px.Constant("28th"),
                      labels=dict(x="Periods of time", y="Amount of fixed", color="Day"))
        fig.add_bar(x=hours, y=fix_count, name="24th")
        fig.write_html("templates/bikefix.html")
        return render(request, '../templates/manager_bikefix_plot.html')