from django.shortcuts import render , get_object_or_404,Http404
from django.template import loader
from django.http import HttpResponse
from django.utils.text import slugify
from .models import New

# Create your views here.

def news(request):
    news = New.objects.all().values()
    return render(request, 'index.html', {'news': news})
def newDetail(request,title):
    try:   
        the_title = title.replace("-"," ")
        new = New.objects.get(title=title)
        template = loader.get_template('newdetail.html')
        context = {
            'new': new
        }
        return HttpResponse(template.render(context, request))

    except New.DoesNotExist:
        raise Http404("New does not exist")