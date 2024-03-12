from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Index_carousel,Skils,About,Courses,Popular_courses,Instructors,Clients
from .forms import ContactForm

# Create your views here.

def index(request):
   home1 = Index_carousel.objects.all()
   home2 = Skils.objects.all()
   home3 = About.objects.all()
   home4 = Courses.objects.all()
   home5 = Popular_courses.objects.all()
   home6 = Instructors.objects.all()
   home7 = Clients.objects.all()
   context = {
      'home1' : home1,
      'home2' : home2,
      'home3' : home3,
      'home4' : home4,
      'home5' : home5,
      'home6' : home6,
      'home7' : home7
   }
   return render(request, 'index.html', context=context)




def about(request):
   about1 = Skils.objects.all()
   about2 = About.objects.all()
   about3 = Instructors.objects.all()
   context = {
      'about1' : about1,
      'about2' : about2,
      'about3' : about3
   }
   return render(request, 'about.html', context=context)


def courses(request):
   courses1 = Courses.objects.all()
   courses2 = Popular_courses.objects.all()
   courses3 = Clients.objects.all()
   context = {
      'courses1' : courses1,
      'courses2' : courses2,
      'courses3' : courses3
   }
   return render(request, 'courses.html', context=context)


def team(request):
   team = Instructors.objects.all()
   context = {
      'team' : team
   }
   return render(request, 'team.html', context=context)


def testimonial(request):
   client = Clients.objects.all()
   context = {
      'client' : client
   }
   return render(request, 'testimonial.html', context=context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Sizning malumotingiz qabul qilindi</h1>")
    context = {
        'form': form
    }
    return render(request,'contact.html',context=context)




def detail1(request,home1):
    home1 = get_object_or_404(Index_carousel, slug=home1)
    context = {
        'home1': home1
    }
    return render(request,'detail1.html',context=context)



def detail3(request,home3):
    home3 = get_object_or_404(About, slug=home3)
    context = {
        'home3': home3
    }
    return render(request,'detail3.html',context=context)

def detail4(request,home4):
    home4 = get_object_or_404(Courses, slug=home4)
    context = {
        'home4': home4
    }
    return render(request,'detail4.html',context=context)

def detail5(request,home5):
    home5 = get_object_or_404(Popular_courses, slug=home5)
    context = {
        'home5' : home5
    }
    return render(request,'detail5.html',context=context)


def detail6(request,home6):
    home6 = get_object_or_404(Instructors, slug=home6)
    context = {
        'home6' : home6
    }
    return render(request,'detail6.html',context=context)


def detail7(request,home7):
    home7 = get_object_or_404(Clients, slug=home7)
    context = {
        'home7' : home7
    }
    return render(request,'detail7.html',context=context)


def error(request):
    context = {
        'error' : error
    }
    return render(request,'404.html', context=context)