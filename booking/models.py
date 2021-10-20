from django.db import models

BASE_PRICE = 200.00
SUITE_SURCHARGE = 0.25
OCEAN_SURCHARGE = 0.40


# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    price = models.FloatField(default=BASE_PRICE)
    occupied = models.BooleanField(default=False)
    oceanside = models.BooleanField(default=False)
    suite = models.BooleanField(default=False)

    def __str__(self):
        return "Room #" + str(self.room_num)


class Guest(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    vip = models.IntegerField(default=-1)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first + " " + self.last

    def get_absolute_url(self):
        return '/guestlist'


class Employee(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    empid = models.IntegerField(default=-1)
    position = models.CharField(max_length=100)
    salary = models.FloatField(default=25.00)

    def __str__(self):
        return self.first + " " + self.last

    def get_absolute_url(self):
        return '/employeelist'

    pass

class Stay(models.Model):
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.guestid.first + " " + self.guestid.last + " staying in room #" + str(self.roomid.room_num) + \
               " from " + str(self.start.month) + "/" + str(self.start.day) + " until " + str(self.end.month) + "/" + \
               str(self.end.day) + ". \n Attending Concierge: " + self.empid.first + " " + self.empid.last