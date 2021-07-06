import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import myanalysis.p108


def home(request):
    return render(request, 'home.html')
def c1(request):
    return render(request, 'c1.html')
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
    return render(request, 'iotsresult.html')

