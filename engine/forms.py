from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    country = forms.CharField(label='Страна')
    city = forms.CharField(label='Город')
    street = forms.CharField(label='Улица')
    number_of_house = forms.IntegerField(label='Номер дома')