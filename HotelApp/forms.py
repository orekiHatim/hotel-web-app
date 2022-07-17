from logging import PlaceHolder
from django.core import validators
from django import forms
from .models import *


class RoomsRegistrations(forms.ModelForm):
    class Meta:
     model = Rooms
     fields = ['RoomNumber', 'CollectionId', 'RoomImage']
     widgets = {
         'RoomNumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'RoomNumber'}),
         'CollectionId': forms.Select(attrs={'class': 'form-control', 'placeholder':'CollectionId'}),
         'RoomImage': forms.FileInput(attrs={'class': 'form-control'}),        
     }



class CollectionsRegistrations(forms.ModelForm):
    class Meta:
     model = Collections
     fields = ['CollectionName', 'CollectionDescription', 'Tv','Clima','Shower','Wifi','Pool','Balcony','Breakfast','Dinner','KingSize','QueenSize','SingleSize','Stars','price']
     widgets = {
         'CollectionName': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'CollectionName'}),
         'CollectionDescription': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'CollectionDescription'}),
         'Tv': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Tv'}),
         'Clima': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Clima'}),
         'Shower': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Shower'}),
         'Wifi': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Wifi'}),
         'Pool': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Pool'}),
         'Balcony': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Balcony'}),
         'Breakfast': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Breakfast'}),
         'Dinner': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Dinner'}),
         'KingSize': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder':'KingSize'}),
         'QueenSize': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder':'QueenSize'}),
         'SingleSize': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder':'SingleSize'}),
         'Stars': forms.Select(attrs={'class': 'form-control ', 'placeholder':'Stars'}),
         'price': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder':'price'}),

     }