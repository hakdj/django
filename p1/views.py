import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import myanalysis.p108
from myanalysis.part4 import P109


def home(request):
    return render(request, 'home.html');
def c1(request):
    return render(request, 'c1.html');
def c1data(request):
    data = myanalysis.p108.P108().p108();
    return HttpResponse(json.dumps(data), content_type='application/json');
    #여기서는 페이지 이동이 아니라 데이터를 셋팅해서 보내주는 역할을 함

def iots(request):
    speed=request.GET['speed'];
    rpm=request.GET['rpm'];
    temp=request.GET['temp'];
    logger = logging.getLogger('users');
    logger.debug(','+speed+','+rpm+','+temp);
    return render(request, 'iotsresult.html');

def jpgs(request):
    P109().mat01();
    return render(request, 'jpgs.html');

def maps(request):
    P109().mat07();
    return render(request, 'seoul_map.html');

def chart1(request):
    return render(request, 'chart1.html');
def chart1s(request):
    location = request.GET['location'];
    P109().mat11(location);
    return render(request, 'chart1result.html');

def chart2(request):
    return render(request, 'chart2.html');

def chart2s(request):
    sy=request.GET['sy'];
    ey=request.GET['ey'];
    ns=request.GET['ns'];
    print(sy,ey,ns);
    data= P109().mat03(sy,ey);
    return HttpResponse(json.dumps(data), content_type='application/json');


def chart3(request):
    P109().mat10();
    return render(request, 'chart3.html');

def chart4(request):
    return render(request, 'chart4.html');
def chart4s(request):
    year = request.GET['year'];
    P109().mat09(int(year));
    return render(request, 'chart4result.html');