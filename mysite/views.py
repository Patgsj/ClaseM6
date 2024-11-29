from mysite.forms import ContactForm

from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    # first_name='Sergio'
    # last_name=' Henriquez'
    # context={'first_name':first_name, 'last_name':last_name}
    # return render(request, 'home.html', context)
    return render(request, 'home.html')

def contact (request):
    # # now=datetime.datetime.now
    # # return render(request, 'contact.html', context={'date_now': now})
    # if request.method == 'POST':
    #    form = ContactForm(request.POST)
    #    print ('***' ,request.method)
    #    print(request.POST)

    # else:

    #     form = ContactForm()
     
    
    
    # return render(request,  'contact.html', context={'form':form})
     return render(request,  'contact.html')

def about (request):
     return render(request, 'about.html')

def testimonials(request):
    testimonials=[
         {
             'name':'Maria',
             'testimonial':'Exelente servicio'
         },
         {
             'name':'Juan',
             'testimonial':'No me gusto la pagina'
         }]
    return render(request, 'testimonials.html', context={'data':testimonials})




