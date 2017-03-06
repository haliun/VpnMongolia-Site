from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class Registrationform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','password1','password2')
    def save(self,commit=True):
            user=super(Registrationform,self).save(commit=False)
            user.email=self.cleaned_data['email']
        
            if commit:
                user.save()
            return user
class ContactForm(forms.Form):
	name=forms.CharField(required=True)
	email=forms.CharField(required=True)
	subject=forms.CharField(required=True)
	message=forms.CharField(required=True,widget=forms.Textarea)