from django import forms

class PolleriaForm(forms.Form):
    tipo1 = forms.CharField(label='Tipo 1',max_length=100)
    tipo2 = forms.CharField(label='Tipo 2',max_length=100)
    complemento = forms.ChoiceField(label='complemento',choices=[('Arroz','Arroz'),('Sopa','Sopa'),('Anticuchos','Anticuchos')])

    
    
    
