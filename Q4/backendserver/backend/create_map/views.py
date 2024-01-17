from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
from datetime import datetime, timedelta
# from background_task import backgorund
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
import time
import requests


scheduler = BackgroundScheduler()

# from .task import my_scheduled_task
@api_view(['POST'])
def calculate_price(request):
    body = json.loads(request.body)
    total_price = 0
    parcels=body['parcels']
    temperature_condition=body['temperature_condition']
    for parcel in parcels:
        length = parcel['length']
        width = parcel['width']
        height = parcel['height']

        weight = length*height*width/5000
        price =0
        if(temperature_condition=="Ambient"):
            if(weight<=5):
                price=10
            else:
                price=15
        elif(temperature_condition=="Chill"):
            if(weight<=5):
                price=20
            else:
                price=30
        print(price)
        total_price += price
    return Response(total_price)
