from django import forms


class search_city(forms.Form):
    city = forms.CharField(max_length=40)