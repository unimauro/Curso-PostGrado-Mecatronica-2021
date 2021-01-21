from django import forms

class SalchisForm(forms.Form):
    tipo1 = forms.CharField(label='Tipo 1', max_length=100)
    tipo2 = forms.CharField(label='Tipo 2', max_length=100)
    salsa = forms.ChoiceField(label='Salsa', choices=[('todo','Todo'),('SinKepchut','Sin Kepchut'),('nada','Nada')])
