from django.shortcuts import render, redirect
from .models import Congratulation, Rasmlar
from .forms import CongratulationForm

def home(request):
    congratulations = Congratulation.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = CongratulationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CongratulationForm()
    return render(request, 'home.html', {'congratulations': congratulations, 'form': form})


def view_teacher(request):
    congratulations = Congratulation.objects.all()
    rasmlar = Rasmlar.objects.all()

    return render(request, 'viewreports.html', {'congratulations': congratulations,'rasmlar': rasmlar},)