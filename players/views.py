from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Player
from .forms import PlayerForm


# Create your views here.
def index(request):
  return render(request, 'players/index.html', {
    'players': Player.objects.all()
  })

def view_player(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = PlayerForm(request.POST)
    if form.is_valid():
      new_player_number = form.cleaned_data['player_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_role = form.cleaned_data['role']
      new_subscription = form.cleaned_data['subscription']

      new_player = Player(
        player_number=new_player_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        role=new_role,
        subscription=new_subscription
      )
      new_player.save()
      return render(request, 'players/add.html', {
        'form': PlayerForm(),
        'success': True
      })
  else:
    form = PlayerForm()
  return render(request, 'players/add.html', {
    'form': PlayerForm()
  })


def edit(request, id):
  if request.method == 'POST':
    player = Player.objects.get(pk=id)
    form = PlayerForm(request.POST, instance=player)
    if form.is_valid():
      form.save()
      return render(request, 'players/edit.html', {
        'form': form,
        'success': True
      })
  else:
    player = Player.objects.get(pk=id)
    form = PlayerForm(instance=player)
  return render(request, 'players/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    player = Player.objects.get(pk=id)
    player.delete()
  return HttpResponseRedirect(reverse('index'))
