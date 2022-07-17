from audioop import reverse
import collections
from pyexpat import model
from django.db import connection
from django.shortcuts import render, redirect , HttpResponseRedirect
from django.template import context 
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import RoomsRegistrations,CollectionsRegistrations
import datetime
from django.views.generic import CreateView


# Create your views here.

def AddModel(request,name):
    """
    md  = ''
    collist = Collections.objects.all()
    if(name == "rooms"):
        md = 'Rooms'
        # r = Rooms()
        if request.method == 'POST':
           cursor = connections['default'].cursor()
           cursor.execute("INSERT INTO `hotelapp_rooms` (`RoomNumber`,`CollectionId_id`,`RoomImage`) VALUES( %s , %s , %s )", [request.POST.get('number'), request.POST.get('colid') , request.FILES['image']])

    elif(name == "collections"):
         md = 'Collections'
         if request.method == 'POST':
             ar = CollectionsRegistrations(request.POST)
             if ar.is_valid():
                ar.save()
         else:
             ar = CollectionsRegistrations()        
    context  =  {'modelname':md,'collist':collist }
    return render(request, 'addmodel.html', context)"""
    modelName = ""
    if(name == "rooms"):
        modelName = "Rooms"
        if request.method == 'POST':
            ar = RoomsRegistrations(request.POST)
            if ar.is_valid():
               ar.save()
        else:
            ar = RoomsRegistrations()
    elif(name == "collections"):
        modelName = "Collections"
        if request.method == 'POST':
            ar = CollectionsRegistrations(request.POST)
            if ar.is_valid():
               ar.save()
        else:
            ar = CollectionsRegistrations()   
    return render(request, 'addmodel.html', {'form':ar, 'modelName' : modelName})


"""class AddRooms(CreateView):
    model = Rooms
    form_class = RoomsRegistrations
    template_name = 'addmodel.html'
    success_url = reverse_lazy('adminpanel')"""

def DeleteModel(request,name, id):
        if request.method == 'POST':
            if name == 'rooms':
                pi = Rooms.objects.get(pk = id)
                pi.delete()
                return redirect('collectionsandrooms')
            elif name == 'reservations':
                  pi = Reservations.objects.get(pk = id)
                  pi.delete()
                  return HttpResponseRedirect(reverse('modellist', kwargs={'name': 'reservations'}))
            elif name == 'reservations_history':
                  pi = Reservations_History.objects.get(pk = id)
                  pi.delete()
                  return HttpResponseRedirect(reverse('modellist', kwargs={'name': 'reservations_history'}))
            elif name == 'collections':
                  pi = Collections.objects.get(pk = id)
                  pi.delete()
                  return redirect('collectionsandrooms')
            elif name == 'user':
                  pi = User.objects.get(pk = id)
                  pi.delete()
                  return HttpResponseRedirect(reverse('modellist', kwargs={'name': 'user'}))
            elif name == 'feedback':
                  pi = Feedback.objects.get(pk = id)
                  pi.delete()
                  return HttpResponseRedirect(reverse('modellist', kwargs={'name': 'feedback'}))
            


def home(request):
    return render(request, 'home.html')


def adminpanel(request):
    context = {'test' : 1}
    return render(request,'home.html',context )




def cleaningreservations ():
      Date = datetime.datetime.now()
      Date = str(Date)
      ListDate = Date.split()
      CurrentDate = ListDate[0]
      query = Reservations.objects.raw("Select * from HotelApp_Reservations where DateF < %s ", [CurrentDate])
      for e in query:
        HistoryObject = Reservations_History.objects.create(ClientId = e.ClientId, roomId = e.roomId, DateD = e.DateD, DateF = e.DateF, Total = e.Total)
        HistoryObject.save()
        e.delete()

def ModeLlist(request,name):
    context = None
    if(name == "reservations"):
        cleaningreservations ()
        mycount = Reservations.objects.count()
        model = Reservations.objects.all()
        context = {'modellist' : model,'mycount':mycount,'test':model.model.__name__}
    elif(name == "reservations_history"):
        cleaningreservations ()
        mycount = Reservations_History.objects.count()
        model = Reservations_History.objects.all()
        context = {'modellist' : model,'mycount':mycount,'test':model.model.__name__}
    elif(name == "user"):
        mycount = User.objects.filter(is_staff=0).count()
        model = User.objects.filter(is_staff=0)
        context = {'modellist' : model,'mycount':mycount,'test':model.model.__name__}
    elif(name == "dashboard"):
        roomsCount = len(Rooms.objects.all())
        reservationsCount = len(Reservations.objects.all())
        collectionsCount = len(Collections.objects.all())
        reservations_historyCount = len(Reservations_History.objects.all())
        usersCount = len(User.objects.filter(is_staff=0))
        rooms = Rooms.objects.all().order_by('-id')[:5]
        reservations = Reservations.objects.all().order_by('-id')[:5]
        collections = Collections.objects.all().order_by('-id')[:5]
        reservationsHistory = Reservations_History.objects.all().order_by('-id')[:5]
        users = User.objects.filter(is_staff=0).order_by('-id')[:5]
        context = {'roomsCount':roomsCount,'reservationsCount':reservationsCount,'collectionsCount':collectionsCount,'reservations_historyCount':reservations_historyCount,'usersCount':usersCount,'rooms':rooms,'reservations':reservations,'collections':collections,'reservationsHistory':reservationsHistory,'users':users}
        return render(request,'dashboard.html',context)
        
    return render(request,'modellist.html',context)
    
    

def CollectionsandRooms(request):
    col = Collections.objects.all()
    rmcount = Rooms.objects.count()
    context = {'collist' : col,'rmcount' : rmcount,}
    return render(request,'Collections.html',context)




def EditView(request, name, id):
    model = Rooms.objects.all()
    context = {'model' : model}
    return render(request,'edit.html' , context)