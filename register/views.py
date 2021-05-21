from django.shortcuts import render,redirect

# Create your views here.
from .forms import UserRegisterForm,UserBookingForm
from django.contrib import messages
from django.contrib.auth.models import User

from advisor.models import Post

from .models import Booking
from django.contrib.auth.decorators import login_required

context = []
for obj in Post.objects.all():
    context.append(obj.Name)
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

# Create your views here.
@login_required
def book(request):

    if request.method =="POST":
        form = UserBookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('Advisor')
            if name in context:
                form.save()
                messages.success(request, f'Call has been booked with {name}!')
                return redirect('home')
            else:
                messages.info(request, f'Please fill correct Advisor name!')
                return redirect('book')

    else:
        form = UserBookingForm(request.POST)

    return render(request, 'booking.html', {'form':form})

@login_required
def bookinglist(request):
    lis = Booking.objects.all()


    return render(request, 'bookinglist.html', {'lis':lis})
