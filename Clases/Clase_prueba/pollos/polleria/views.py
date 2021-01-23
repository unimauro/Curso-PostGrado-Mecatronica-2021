from django.shortcuts import render
from .form import PolleriaForm

# Create your views here.
def home(request):
    return render(request,'polleria/home.html')

def orden(request):
    if request.method =='POST':
        filled_form=PolleriaForm(request.POST)
        if filled_form.is_valid():
            note = "Gracias por enviar su ORDEN: %s , %s,  %s" %(filled_form.cleaned_data['complemento'],filled_form.cleaned_data['tipo2'],filled_form.cleaned_data['tipo1'],)
            new_form = PolleriaForm()
            return render(request,'polleria/orden.html',{'polleriaform':new_form,'note':note})            
    else:
        form = PolleriaForm()
        return render(request,'polleria/orden.html',{'polleriaform':form})