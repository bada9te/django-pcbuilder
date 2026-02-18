from django.forms import ModelForm
from .models import PcBuild, User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class PcBuildForm(ModelForm):
    class Meta:
        model = PcBuild
        fields = ['box', 'motherboard', 'cpu', 'gpu', 'ram', 'storage', 'psu']
