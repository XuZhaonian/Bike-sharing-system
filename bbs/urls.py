"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bikesharing import views
from bikesharing import checkuser
from bikesharing import tests
from bikesharing import bikemap
from bikesharing import bikemanage
from bikesharing import bikefix
from bikesharing import bikeprice
from bikesharing import bikeusingtimes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', checkuser.userLog.login),
    path('logup/', checkuser.userLog.logup),
    path('customer/', checkuser.userLog.index_customer),
    path('operator/', checkuser.userLog.index_operator),
    path('manager/', checkuser.userLog.index_manager),
    path('getbike/', bikemap.bikemap.getbikepos),
    path('makemap/', bikemap.bikemap.makemap),
    path('manager/bikemap/', bikemap.bikemap.showmap),
    path('manager/gettable/', bikemanage.bikemanage.gettable),
    path('manager/biketable/', bikemanage.bikemanage.chosetable),
    path('manager/showinitialplot/', bikefix.bikefix.showinitialplot),
    path('manager/getfixdata/', bikefix.bikefix.getfixdata),
    path('manager/showinitialpriceplot/', bikeprice.bikeprice.showinitialplot),
    path('manager/showchosepriceplot/', bikeprice.bikeprice.showchoseplot),
    path('manager/showinitialusedplot/', bikeusingtimes.bikeusingtimes.showinitialplot),
    path('manager/showchoseusedplot/', bikeusingtimes.bikeusingtimes.showchoseplot),
    path('teststilllogin/', checkuser.userLog.teststilllogin),
    path('logout/', checkuser.userLog.logout),
    # path('test/', bikefix.bikefix.showinitialplot),
    path('test/', views.write_route),
    # path('session_test/', tests.session_test),
    # path('googlemap/', tests.showmap),
]
