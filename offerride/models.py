from django.db import models

"""class Driver(models.Model):
	uname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	fname = models.CharField(max_length=250)
	lname = models.CharField(max_length=250)
	psw  = models.CharField(max_length=240)
	def __str__(self):
		return self.uname"""


class Car(models.Model):
	carseats = models.IntegerField(default=0,null = True)
	color= models.CharField(max_length=240, default='red',null = True)
	carno = models.CharField(max_length=250, default="x",null = True)
	carmodel= models.CharField(max_length=250, default='x',null = True)
	cartype = models.CharField(max_length=250,default='s',null = True)
	def __str__(self):
		return self.carno

class Ride(models.Model):
	#driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
	#driverid = models.CharField(max_length=250, default='rnk')
	username = models.CharField(max_length=250,default='rnk')
	startpoint = models.CharField(max_length=250)
	endpoint = models.CharField(max_length=250)
	ipoint1 = models.CharField(max_length=250)
	ipoint2 = models.CharField(max_length=250)
	date = models.CharField(max_length =250, default='23/3/2019')
	time = models.CharField(max_length =250, default='10:10')
	price = models.IntegerField(default = 0)
	seat = models.IntegerField(default = 1)

	def __str__(self):
		return self.startpoint + '-' + self.endpoint
 
