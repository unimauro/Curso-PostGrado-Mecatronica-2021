from django.shortcuts import render
from .forms import SalchisForm

# Create your views here.
def home(request):
    return render(request,'salchis/home.html')

def order(request):
    if request.method == 'POST':
        filled_form=SalchisForm(request.POST)
        if filled_form.is_valid():
            note = 'Gracias por Ordenar %s , %s,  %s su Salchipapa' %(filled_form.cleaned_data['salsa'],filled_form.cleaned_data['tipo2'],filled_form.cleaned_data['tipo1'],)
            new_form =SalchisForm()
            return render(request,'salchis/order.html',{'salchisform':new_form,'note':note})
    else:
        form =SalchisForm()
        return render(request,'salchis/order.html',{'salchisform':form})