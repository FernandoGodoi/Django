# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord

from django.http import HttpResponse

# Create your views here.

def index(request):
    lista_paginas = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": lista_paginas}

    return render(request, 'first_app/index.html', context=date_dict)