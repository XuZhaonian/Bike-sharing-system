from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import BikeAttribute, BikeState


class bikemanage:
    def showtable(request):
        return render(request, '../templates/manager_biketable.html')

    def gettable(request):
        if request.method == "POST":
            choice = request.POST.get("bikestate", None)
            print(choice)
            request.session['choice'] = choice
            return redirect("/manager/biketable/")
        else:
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.all()
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            # return redirect("/manager/biketable/")
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})

    def chosetable(request):
        choice = request.session['choice']
        if choice == "all":
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.all()
            print("get the choice all")
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})
        elif choice == "accessible":
            bs = BikeState.objects.get(state_id=1)
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.filter(bike_state=bs)
            print("get the choice accessible")
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})
        elif choice == "using":
            bs = BikeState.objects.get(state_id=2)
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.filter(bike_state=bs)
            print("get the choice accessible")
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})
        elif choice == "unaccessible":
            bs = BikeState.objects.get(state_id=3)
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.filter(bike_state=bs)
            print("get the choice accessible")
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})
        elif choice == "fixing":
            bs = BikeState.objects.get(state_id=4)
            bikeinfolist = []
            bike_att_list = BikeAttribute.objects.filter(bike_state=bs)
            print("get the choice accessible")
            for i in bike_att_list:
                bikeinfolist.append([i.bike_id, i.bike_state.state_name,
                                     (i.bike_stationx, i.bike_stationy)])
            return render(request, '../templates/manager_biketable.html', {"bikelist": bikeinfolist})
        else:
            return HttpResponse("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
