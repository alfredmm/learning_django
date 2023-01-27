from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing (request):
    #mydata = Member.objects.all().order_by('last_name', "-id").values()
    #mydata = Member.objects.all().order_by('-first_name').values() - Descending use Minus sign
    #mydata = Member.objects.all().order_by('first_name').values() - Ascending
    #mydata = Member.objects.filter(first_name__startswith = 'L').values()
    #mydata = Member.objects.filter(Q(first_name= 'Alfred') | Q(first_name = 'Mike'))
    #mydata = Member.objects.filter(first_name = 'Alfred') | Member.objects.filter(first_name= "Mike")
    #mydata = Member.objects.filter(first_name = 'Alfred')
    #filtered_members = Member.objects.filter(first_name= 'Alfred')
    template = loader.get_template('template.html')
    context = {
        #'mymembers' : mydata,
        'fruits': ['Apple', 'Orange', 'Lemon', 'Cherries'],
    }
    return HttpResponse(template.render(context, request))