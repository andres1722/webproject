from django import forms

class newstoreform(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={ 'class':'textimp'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={ 'class':'textimp'}))

class newproductform(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={ 'class':'textimp'}))
    price = forms.FloatField(label='Price', widget=forms.NumberInput(attrs={ 'class':'textimp'}))
    store = forms.CharField(label='Store', max_length=100, widget=forms.TextInput(attrs={ 'class':'textimp'}))

class contactform(forms.Form):
    email = forms.CharField(label='EMail', max_length=100, widget=forms.TextInput(attrs={ 'class':'textimp'}))
from .models import Comment  # asegurate de tener esto al principio si no está

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'textimp'}),
            'text': forms.Textarea(attrs={'placeholder': 'Escribí tu comentario...', 'class': 'textimp'}),
        }
