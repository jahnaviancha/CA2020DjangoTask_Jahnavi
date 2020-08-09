from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms
from . import forms
from . import models


# Create your views here.

def index(request):
    # form=forms.Registerform
    if request.method == 'POST':
        form=forms.Registerform(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('blog')
            except:
                print("Error")
    else:
        form=forms.Registerform()
        # print("name" + form.cleaned_data['name'])
        # print("password" + form.cleaned_data['password'])
    return render(request, "index.html", {'form': form})


def blog(request):
    return render(request, "blog.html")
