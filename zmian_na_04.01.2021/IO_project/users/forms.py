from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import Account
from django import forms
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # birthDate = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'birthDate', 'country']
        widgets = {
            'birthDate': forms.DateInput(attrs={'type': 'date', 'format': '%d-%m-%Y'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email', 'subscription',
                  'first_name', 'last_name', 'birthDate', 'country']
        widgets = {
            'birthDate': forms.DateInput(attrs={'type': 'date', 'format': '%d-%m-%Y'}),
        }

# country = CountryField()
#     birthDate = models.DateField(null=True)
#     subscription = models.BooleanField(default=False)
#     # boughtMovies = ArrayField(models.IntegerField(
#     #     null=True, blank=True), null=True, blank=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30,)
