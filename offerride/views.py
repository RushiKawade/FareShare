from django.http import HttpResponse
from django.shortcuts import render
from .models import Ride,Car
from django.contrib.auth.models import User



def index(request):
	return render(request,'offerride/index.html')


def addride(request):
	return render(request,'offerride/addride.html')

def submitride(request):
	print("form is submitted")
	startpoint = request.POST.get("startpoint")
	endpoint = request.POST.get("endpoint")
	ipoint1 = request.POST.get("ipoint2")
	ipoint2 = request.POST.get("ipoint2")
	date = request.POST.get("date")
	time = request.POST.get("time")
	seat = request.POST.get("seat")
	price = request.POST.get("price")
	username = None
	#if request.user.autheticated():
	username = request.user.username
	print(username)	
	ride = Ride(username=username,startpoint=startpoint,endpoint=endpoint,ipoint1=ipoint1,ipoint2=ipoint2,date=date,time=time,seat=seat,price=price)
	ride.save()
	print("saved")
	return render(request,'offerride/addride.html')

prev=0
def join(request):
	all_rides = Ride.objects.all()
	template = loader.get_template('offerride/rides.html')
	context = {'all_rides': all_rides}
	reduce_seat = all_rides.get(pk=request.POST['join'])
	print(reduce_seat.pk)
	if reduce_seat.pk !=prev:
		reduce_seat.seat = reduce_seat.seat - 1
		reduce_seat.save()
	return  HttpResponse(template.render(context,request))

def addcar(request):
	return render(request,'offerride/addcar.html')


def submitcar(request):
	print(" Car form is submitted")
	carno = request.POST.get("carno")
	carmodel = request.POST.get("carmodel")
	color = request.POST.get("color")
	cartype = request.POST.get("cartype")
	carseats=request.POST.get("carseats")
	car = Car(carseats = carseats,color= color, carno = carno, carmodel=carmodel, cartype=cartype)
	car.save()
	print("Car saved")
	return HttpResponse("SAVED")


def rides(request):
	startpoint = request.POST.get("startpoint")
	endpoint = request.POST.get("endpoint")
	date = request.POST.get("date")
	all_rides = Ride.objects.all()
	context = {'all_rides': all_rides,
				'startpoint' : startpoint,
				'endpoint' : endpoint,
				'date' : date,

	}
	return render(request,'offerride/rides.html',context)

