from django.shortcuts import render, get_object_or_404, redirect
from .models import Signal
from .serailizer import SignalSerializer
from rest_framework import viewsets
from django.views.generic import DetailView
from django.core.signals import request_finished
from django.dispatch import receiver
from .forms import SignalForm

def home(request):
    form = SignalForm(request.POST or None)
    signal= Signal.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'home.html', {'signal':signal, 'form':form})
@receiver(request_finished)
def signalTest(sender, **kwargs):
    print('en don come ooh!')

def details(request, id):
    signal = get_object_or_404(Signal, id=id)
    return render(request, 'detail.html', {'signal':signal})



class Api(viewsets.ModelViewSet):
    queryset = Signal.objects.all()
    serializer_class = SignalSerializer