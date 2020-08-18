from django.shortcuts import render

import subprocess

from django_cowsay.models import CowsayInputModel
from django_cowsay.forms import CowsayForm
# Create your views here.


def cowsayinput(request):
    if request.method == "POST":
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayInputModel.objects.create(
                text=data.get('text')
                )
            i_say = subprocess.run(["cowsay", data.get('text')], capture_output=True, text=True)
            return render(request, "index.html", {"form": CowsayForm(), "i_say": i_say.stdout})

    form = CowsayForm()
    return render(request, "index.html", {"form": form})

def history(request):
    history = CowsayInputModel.objects.all()
    return render(request, "history.html", {"history": history})

