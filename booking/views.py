from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Room, Guest, Employee, Stay
from .forms import GuestCreateForm, EmployeeCreateForm, StayCreateForm
from .forms import GuestUpdateForm, EmployeeUpdateForm

# Create your views here.


class GuestUpdate(UpdateView):
    model = Guest
    template_name = 'booking/guest_update_form.html'
    form_class = GuestUpdateForm


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'booking/employee_update_form.html'
    form_class = EmployeeUpdateForm


class GuestCreate(CreateView):
    model = Guest
    template_name = 'booking/guest_create_form.html'
    form_class = GuestCreateForm


class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'booking/employee_create_form.html'
    form_class = EmployeeCreateForm


class StayCreate(CreateView):
    model = Stay
    template_name = 'booking/templates/registration/stay_create_form.html'
    form_class = StayCreateForm


class RoomList(ListView):
    model = Room


class GuestList(ListView):
    model = Guest


class EmployeeList(ListView):
    model = Employee


def home(request):
    # templates folder is already assumed b/c this app is registered in settings.py
    name = Homer
    loggedin=False
    context = {"user_first_name": name, "rooms":ROOMS, "loggedin":loggedin}
    return render(request, 'booking/home.html', context=context)

@login_required()
def about(request):
    return render(request, 'booking/about.html')


class GuestDelete(DeleteView):
    model = Guest
    template_name = 'booking/guest_delete_form.html'
    success_url = '/guestlist'


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'booking/employee_delete_form.html'
    success_url = '/employeelist'