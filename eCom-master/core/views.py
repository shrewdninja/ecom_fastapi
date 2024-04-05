from django.shortcuts import render, redirect
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib import messages
from item.models import Category, Item
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm, FeedbackForm,CustomChangePasswordForm
# Create your views here.

def index(request):
    items=Item.objects.filter(is_sold=False)[0:8]
    categories=Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items
    })


def changepasswordview(request):
    if request.method == 'POST':
        form = CustomChangePasswordForm(request.user,request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            # messages.success(request,
            #                  'Your password was successfully updated!',
            #                  extra_tags='alert-success')
            return redirect('/')
    else:
        form = CustomChangePasswordForm(user=request.user)
    return render(request, 'core/changepassword.html', {'form': form})

def contact(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.save()
            
            return redirect('/')
        
            
    else:
        form = FeedbackForm()
    return render(request, 'core/contact.html', {'form': form, 'title': 'Feedback Form'})



def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')

