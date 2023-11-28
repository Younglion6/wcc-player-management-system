from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
  class Meta:
    model = Player
    fields = ['player_number', 'first_name', 'last_name', 'email', 'role', 'subscription']
    labels = {
      'player_number': 'Player Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'role': 'Role',
      'subscription': 'Subscription',
    }
    widgets = {
      'player_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'role': forms.TextInput(attrs={'class': 'form-control'}),
      'subscription': forms.TextInput(attrs={'class': 'form-control'}),
    }
