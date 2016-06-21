from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Booking, DisabledDates
from .forms import BookingForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import json
# Create your views here.
def get_ip(request):
	try:
		x_forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forwarded:
			ip = x_forwarded.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except :
		ip = ""

	return ip

def homepage(request):
	return render(request, 'home.html')

#def successfull_booking(request):
#	return render(request, 'successful_registered.html')


def register(request):
	disableddate = ["2016-06-1"]
	try:
		form = BookingForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.ip_address = get_ip(request)
			instance.user_agent = request.META.get("HTTP_USER_AGENT")
			first_name = request.POST.get('first_name')
			subject = 'Confirmation | Rishabh Consultants'
			message = 'Dear ' + first_name + ',\n' +'\tYour booking has been duly noted. We"ll soon be in touch with your registered mobile or email.'
			from_email = 'rishabhnehrapersonal@gmail.com'
			recipient = request.POST.get('email')
			admin2 = 'anilhnehra@gmail.com'
			instance.save()
			try:
				send_mail(
				    subject,
				    message,
				    from_email,
				    [ recipient, from_email, admin2],
				    fail_silently=False
				)
			except:
				return render(request, 'unsuccessful.html')

			return render(request, 'successful_registered.html', )


	except :
		form = "OT"

	else:
		dates = DisabledDates.objects.all()
		disableddate.extend(dates)
		# js = json.dumps(dates)
		# print (js)
		context = {
			# 'js':js,
			 'dates': dates,
			'form_html':form,
			'disableddate':disableddate
		}
		return render(request, 'booking.html', context)

def showdisableddate(request):
	list = ["2016-06-1"]
	dates = DisabledDates.objects.all()
	list.extend(dates)
	context = {
		'dates': dates,
		'list': list
	}	
	return render(request, 'disableddate.html', context)
