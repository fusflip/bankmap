from django import forms

class Coordinate(forms.Form):
    code = forms.CharField(label='code', max_length=100)
    geocode = forms.CharField(label='geocode', max_length=100)