# from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello, world!</h2>")


def current_date(request):
    now = datetime.now()
    html = '<html><nody>Сегодняшняя дата %s.</body></html>' % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    # assert False
    html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)
