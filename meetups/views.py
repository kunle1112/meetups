
from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm

# Create your views here.

def meetups (request):
    meetups=Meetup.objects.all()
    return render(request, 'meetups/meetups.html', {'meetups':meetups})

def meetup_details(request, meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if request.method=="GET":
           registration_form=RegistrationForm()
        else:
          registration_form=RegistrationForm(request.POST)
          if registration_form.is_valid():
              participant=registration_form.save()
              selected_meetup.participant.add()
              return redirect('confirm-registration')
        return render(request, 'meetups/meetup-details.html', {
           'meet_found':True,
           'form':registration_form,
           'meetup': selected_meetup})
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
           'meet_found':False
        })


def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')