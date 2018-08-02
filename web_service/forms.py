from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
    
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class Profile(forms.ModelForm):
    country = forms.CharField(required = False)
    city = forms.CharField(required = False)
    work_place = forms.CharField(required = False)
    help_with   = forms.CharField(widget = forms.Textarea, required = False)
    need_help_with = forms.CharField(widget = forms.Textarea, required = False)
    contact_info = forms.CharField(widget=forms.Textarea, required = False)
    photo = forms.ImageField(required = False)

    class Meta:
        model = UserProfile
        fields = ("country", "city", "work_place", "help_with", "need_help_with", "contact_info", "photo")


    # def save(self, commit=True):
    #     user = super(Profile, self).save(commit=False)
    #     user.country = self.cleaned_data["country"]
    #     user.city = self.cleaned_data["city"]
    #     if commit:
    #         user.save()