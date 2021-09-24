import null as null
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from numpy import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bikesharing.models import UserReg

from bikesharing import models

def testsession(request):
    if request.method == "POST":
        request.session['username'] = "test"


class userLog:
    # login
    def login(request):
        if request.POST.get("name", None):
            # redirect("/logup/")
            x = 0
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
            # return HttpResponse("Wrong!!!!!!!!!!!!!"):
            return redirect("/login/")

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
            getuser = UserReg(user_name=user['user_name'], user_password=user['user_password'],
                              user_perm_id=user['user_perm'])
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
            return redirect("/getbike/")
            # return render(request, '../templates/index_manager.html')


    def logout(request):
        try:
            del request.session['user_id']
        except KeyError:
            pass
        return HttpResponse("Logged out!!!!!!!!!!")

    def teststilllogin(request):
        if request.session['user_id'] != null:
            usershow = UserReg.objects.get(user_id=request.session['user_id'])
            return 0
        else:
            return 1
        # return render(request, "index_04.html", {'usershow': usershow})
        # return 0