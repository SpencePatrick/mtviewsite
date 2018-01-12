# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import boto3
import calendar
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import WrestlingMatch, Budget, BudgetCategory, StoreMerchandise
from .forms import UploadVideoForm, RegisterForm, ItemForm

# Create your views here.
def index(request):
    # s3 = boto3.resource('s3')
    # for bucket in s3.buckets.all():
    #     print(bucket.name)
    context = {'categories': 'Hello World'}
    return render(request, 'mtview/index.html', context)

def videos(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        allmatches = WrestlingMatch.objects.filter(username=request.user.username)
        print(allmatches)
        context = {'user': request.user, 'videos': allmatches}
    return render(request, 'mtview/videos.html', context)

def video(request, video):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:

        allmatches = WrestlingMatch.objects.filter(username=request.user.username)
        print(allmatches)
        context = {'user': request.user, 'videos': allmatches, 'video': video}
    return render(request, 'mtview/video.html', context)

def videopayment(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        context = {}
    return render(request, 'mtview/videopayment.html', context)

def login(request):
    context = {'categories': 'Hello World'}
    return render(request, 'mtview/login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Need to check if passwords match and then create new user
            print(form.cleaned_data['password'])

            return render(request, 'mtview/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'mtview/register.html', {'form': form})

def roster(request):
    context = {'categories': 'Hello World'}
    return render(request, 'mtview/roster.html', context)

def schoolstore(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['quantity'])
            print(form.cleaned_data)
            cartitems = {
                'quantity': form.cleaned_data['quantity'],
                'size': form.cleaned_data['shirtsizes'],
                'color': form.cleaned_data['colors'],

                }
            merchandise = StoreMerchandise.objects.all()
            context = {'merchandise': merchandise, 'form': form, 'cartitems': cartitems}
            return render(request, 'mtview/schoolstore.html', context)
    else:
        form = ItemForm()

    merchandise = StoreMerchandise.objects.all()
    context = {'merchandise': merchandise, 'form': form}
    return render(request, 'mtview/schoolstore.html', context)

def schedule(request):
    tc=calendar.HTMLCalendar(firstweekday=0)
    context = {'calendar': tc}
    print(tc)
    return render(request, 'mtview/schedule.html', context)

def budgets(request):
    budgets = Budget.objects.all()
    budgetcategories = BudgetCategory.objects.all()
    context = {'budgets': budgets, 'budgetcategories': budgetcategories}
    return render(request, 'mtview/budgets.html', context)

def uploadvideos(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            # Need to upload video to MEDIA_ROOT and change name of file

            return render(request, 'mtview/uploadvideos.html', {'form': form})
    else:
        form = UploadVideoForm()
    return render(request, 'mtview/uploadvideos.html', {'form': form})

# def user_gains_perms(request, userid):
