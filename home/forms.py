from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
	


	#first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'mdl-example__phone'}))
	#last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'mdl-example__phone'}))
	#email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'mdl-example__phone'}))
	#mobile_number = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'mdl-example__phone'}))
	#message = forms.CharField(widget = forms.Textarea(attrs={'class':'mdl-example__phone'}))
	
	
	class Meta:
		model = Booking
		fields = [
			"first_name",
			"last_name",
			"email",
			"mobile_number",
			"company",
			"appointmentstamp",
			"message"
		]
		widgets = { 
			'appointmentstamp': forms.DateInput(attrs={'class': 'datepicker'})
		} 