from django import forms
from .models import *


class PostForm(forms.ModelForm):
	title = forms.CharField(required=True)
	content = forms.CharField(required=True)
	image = forms.ImageField(required=False)
	
	class Meta:
		model = Post
		exclude = [""]