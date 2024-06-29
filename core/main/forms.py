from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Pay,UserMessage



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	

class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ('name', 'card_number', 'hetevi_tver', 'phone_number', 'email')

class AddressForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=50)
    email = forms.EmailField()


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('name','phone', 'email', 'address', 'message')