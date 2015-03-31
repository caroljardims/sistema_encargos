from django import forms
from django.forms import ModelForm
from saldo.models import *

class ProfessorForm(ModelForm):
    class Meta:
	model = Professor
	fields = '__all__'
	
class EncargoForm(ModelForm):
    class Meta:
	model = Encargo
	fields = '__all__'

class MediaForm(ModelForm):
    class Meta:
	model = Media
	fields = '__all__'