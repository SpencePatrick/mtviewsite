from django import forms
from django.contrib.auth.models import User


class UploadVideoForm(forms.Form):
    users = User.objects.all().reverse()
    index = 0
    CHOICES = ()
    for user in users:
        u = ('user' + str(index), str(user.username))
        CHOICES = CHOICES + (u,)
        index += 1

    wrestler = forms.ChoiceField(label='Wrestler', choices=CHOICES)
    videofile = forms.FileField()
    date = forms.DateField()
    opponentschool = forms.CharField(max_length=60)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    passwordagain = forms.CharField(label='Password (again)', max_length=32, widget=forms.PasswordInput)

class BillingForm(forms.Form):
    cc = forms.CharField(max_length=20)
    nameoncard = forms.CharField(max_length=150)
    billingzip = forms.CharField(max_length=5)

class ShippingForm(forms.Form):
    streetaddress1 = forms.CharField(max_length=150)
    streetaddress2 = forms.CharField(max_length=150)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=2)
    zipcode = forms.CharField(max_length=5)

class ItemForm(forms.Form):
    quantity = forms.CharField(max_length = 2)
    SIZES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
    )
    shirtsizes = forms.CharField(label="Size", widget = forms.Select(choices=SIZES))
    COLORS = (
        ('White', 'White'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
    )
    colors = forms.CharField(label="colors", widget = forms.Select(choices=COLORS))
    
