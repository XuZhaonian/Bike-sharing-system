from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from numpy import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import UserReg
from bikesharing.models import BikeFixed
from bikesharing.models import BikeAttribute
from bikesharing.models import BikeState
from bikesharing.models import BikePoint
from bikesharing.models import BikeRoute
import random
import plotly

from bikesharing import models

def testsession(request):
    if request.method == "POST":
        request.session['username'] = "test"


# login
def login(request):
    if request.POST.get("name", None):
        redirect("/logup/")
    else:
        return render(request, '../templates/login.html')
    u = UserReg.objects.get(user_name=request.POST.get("name", None))
    if u.user_password == request.POST.get("password", None):
        request.session['user_id'] = u.user_id
        request.session['user_per'] = u.user_perm_id
        if u.user_perm_id == 1:
            # return render(request, '../templates/index_customer.html', {'uid': u.user_id})
            return redirect("/customer/", {'uid': u.user_id})
        elif u.user_perm_id == 2:
            # return render(request, '../templates/index_operator.html', {'uid': u.user_id})
            return redirect("/operator/", {'uid': u.user_id})
        elif u.user_perm_id == 3:
            # return render(request, '../templates/index_manager.html', {'uid': u.user_id})
            return redirect("/manager/", {'uid': u.user_id})
        else:
            return HttpResponse("Wrong permission!")
    else:
        return HttpResponse("Wrong!!!!!!!!!!!!!")


# register
def logup(request):
    # if request.POST.get("reg_name", None):
    #     redirect("/logup/")
    # else:
    #     return render(request, '../templates/logup.html')
    user = {}
    if request.POST:
        user['user_name'] = request.POST.get("name", None)
        user['user_password'] = request.POST.get("password", None)
        user['user_perm'] = 1
        getuser = UserReg(user_name=user['user_name'], user_password=user['user_password'], user_perm_id=user['user_perm'])
        getuser.save()
        return redirect("/login/")
    return render(request, '../templates/logup.html')


def index_customer(request):
    if request.session['user_id'] == None:
        return redirect("/login/")
    else:
        return render(request, '../templates/index_customer.html')


def index_operator(request):
    if request.session['user_id'] == None:
        return redirect("/login/")
    else:
        return render(request, '../templates/index_operator.html')


def index_manager(request):
    if request.session['user_id'] == None:
        return redirect("/login/")
    else:
        return render(request, '../templates/index_manager.html')


def write_fix(request):
    for i in range(50):
        d = random.randint(1, 28)
        day = str(d)
        hour = str(random.randint(0, 23))
        minute = str(random.randint(0, 59))
        second = str(random.randint(0, 59))
        ftime = "2021-2-" + day + " " + hour + ":" + minute + ":" + second
        fbi = random.randint(1, 500)
        models.BikeFixed.objects.create(fixed_time=ftime, fixed_bike_id=fbi, fixed_operator_id=6)
    return HttpResponse("fix is ok!!!!!!!!!!!!!")


def write_bike(request):
    for i in range(50):
        s = random.randint(0,10)
        bsx = random.uniform(-236.6,-236.5)
        bsy = random.uniform(41.7,41.8)
        if s == 7:
            bs = 2
        elif s == 8:
            bs = 3
        elif s == 9:
            bs = 4
        else:
            bs = 1
        bstate = BikeState.objects.get(state_id=bs)
        bpoint = BikePoint.objects.get(point_id=1)
        BikeAttribute.objects.create(bike_state=bstate, bike_stationx=bsx, bike_stationy=bsy, bike_pointstate=0, bike_pointnum=bpoint)
    return HttpResponse("bike is ok!!!!!!!!!!!!!")

def write_route(request):
    for i in range(50):
        startx = random.uniform(-236.6,-236.5)
        starty = random.uniform(41.7,41.8)
        endx = random.uniform(-236.6,-236.5)
        endy = random.uniform(41.7,41.8)

        day = str(random.randint(1, 28))
        start_hour = str(random.randint(0, 20))
        start_minute = str(random.randint(0, 59))
        start_second = str(random.randint(0, 59))
        start_time = "2021-2-" + day + " " + start_hour + ":" + start_minute + ":" + start_second
        t = random.randint(0,3)
        end_hour = str(int(start_hour) + t)
        end_minute = str(random.randint(0, 59))
        end_second = str(random.randint(0, 59))
        end_time = "2021-2-" + day + " " + end_hour + ":" + end_minute + ":" + end_second

        rb_id = random.randint(1, 20)
        b_id = BikeAttribute.objects.get(bike_id=rb_id)
        bpoint = BikePoint.objects.get(point_id=1)
        bstate = BikeState.objects.get(state_id=1)
        BikeRoute.objects.create(route_bike_id=rb_id, route_starttime=start_time, route_endtime=end_time,
                                 route_price=(t*2), route_bike_state=bstate, route_startx=startx, route_starty=starty,
                                 route_endx=endx, route_endy=endy)
    return HttpResponse("route is ok!!!!!!!!!!!!!")
