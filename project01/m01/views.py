from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    chai_variety = ChaiVariety.objects.all()
    return render(request, 'm01/index.html',{'chai_variety':chai_variety})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'm01/chai_detail.html', {'chai':chai})