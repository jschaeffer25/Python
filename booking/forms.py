from django import forms
from .models import Guest
from.models import Employee

class GuestCreateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first', 'last', 'vip', 'email')


class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first', 'last', 'vip', 'email')


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'empid', 'position', 'salary')


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'empid', 'position', 'salary')