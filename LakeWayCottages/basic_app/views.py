from django.conf import settings
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from basic_app import models
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def index(request):
    feature = models.features.objects.all()
    apartment = models.apartmentType.objects.all()
    return render(request, 'basic_app/index2.html', {'obj': feature, 'apartment': apartment})


class createFeature(CreateView):
    fields = ('image', 'desc')
    model = models.features


class updateFeature(UpdateView):
    fields = ('image', 'desc')
    model = models.features


class deleteFeature(DeleteView):
    context_object_name = 'feature'
    model = models.features
    success_url = reverse_lazy("basic_app:index")


class createApartment(CreateView):
    fields = ('image','ApartmentTitle', 'desc')
    model = models.apartmentType


class updateApartment(UpdateView):
    fields = ('image', 'desc')
    model = models.apartmentType


class deleteApartment(DeleteView):
    context_object_name = 'apartment'
    model = models.apartmentType
    success_url = reverse_lazy("basic_app:index")


def contactMail(request):
    check = False
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(username)
        print(email)
        print(message)
        msg = "Name : " + username + "\n" + "Email : " + email + "\n" + "Message : " + message
        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            ['mwajihrehman@gmail.com'],
            fail_silently=False,
        )


def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Wroong details")

    else:
        return render(request, 'basic_app/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))
