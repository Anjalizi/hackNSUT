from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client

account_sid = 'AC1be5c12bbc465a99586baa2b766fc195'
auth_token = '756d2723cc1ff6dd08351f12f411326f'
client = Client(account_sid, auth_token)

def landing(request):
    return render(request, 'gesture/landing.html')

def movement(request):
    return render(request, 'gesture/gesture-detect.html')

def handwriting(request):
	return render(request, 'gesture/handwriting.html')

def sleep(request):
	return render(request, 'gesture/sleep.html')

def sleepwell(request):
	return render(request, 'gesture/sleepwell.html')

def sms(req):
    return render(req, 'gesture/base.html')

def safe(req):
    message = client.messages \
        .create(
        body="Patient is Safe.",
        from_='+18327261605',
        to='+918851465800'
    )
    print(message.sid)
    return render(req,'gesture/safe.html')

def emergency(req):
    message = client.messages \
        .create(
        body="Please check on patient. EMERGENCY",
        from_='+18327261605',
        to='+918851465800'
    )
    print(message.sid)
    return render(req, 'gesture/unsafe.html')

def send(req):
    message = client.messages \
        .create(
        body="Your Loved One is on the Move.",
        from_='+18327261605',
        to='+918851465800'
    )
    print(message.sid)
    return render(req, 'gesture/success.html')