import datetime, time
from dateutil.relativedelta import relativedelta
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template import Context, loader
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from callapp.serializers import CallSerializer
from callapp.models import Call

def CallBill(request): 
    call_list = Call.objects.all()
    calls = ''
    total = 0
    phone = ''
    period = ''
    if len(request.GET)>0:
        phone = request.GET['phone']
        period = request.GET['period']
    for call in call_list:
        if    ((len(request.GET)==0) and \
                call.timestampend is not None) or \
              ((len(request.GET)>0) and \
                call.type == 1 and \
                call.source == phone and \
                ((period == '' and \
                   call.timestampend.year == (datetime.datetime.now()-relativedelta(months=1)).year and \
                   call.timestampend.month == (datetime.datetime.now()-relativedelta(months=1)).month) or \
                 (period != '' and \
                  call.timestampend.year == int('20'+period[-2:]) and \
                  call.timestampend.month == int(period[:2])))):
            calls += ('<tr height=30>'+ 
		      '<td>'+str(call.id)+'</td>'+ 
		      '<td>'+call.timestampstart.strftime('%m-%d-%Y %H:%M:%S')+'</td>'+ 
		      '<td>'+call.timestampend.strftime('%m-%d-%Y %H:%M:%S')+'</td>'+ 
		      '<td>'+call.source+'</td>'+ 
		      '<td>'+call.destination+'</td>'+ 
		      '<td>'+call.duration+'</td>'+ 
		      '<td>U$ '+str(call.price)+'</td>'+ 
		      '</tr>')
            total+=float(call.price)
    calls += ('<tr height=30>'+ 
              '<td colspan=6><b>Total</b></td>'+ 
              '<td width=150><b>U$ '+("%0.2f" % round(total,2))+'</b></td>'+ 
              '</tr>')
    context = {"call_list": call_list, 
               "calls": calls}
    return render(request, "callapp/call_bill.html",context)
    
class CallList(ListView):
    model = Call

class CallCreateForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['timestampstart', 'timestampend', 'source', 'destination']
        widgets = {
        'timestampstart': forms.TextInput(attrs={'readonly':True, 'value':datetime.datetime.now}),
        'timestampend': forms.TextInput(attrs={'readonly':True}),
        }

class CallCreate(CreateView):
    model = Call
    form_class = CallCreateForm
    success_url = reverse_lazy('call_list')

class CallUpdateForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['timestampstart', 'timestampend', 'source', 'destination']
        widgets = {
        'timestampstart': forms.TextInput(attrs={'readonly':True}),
        'timestampend': forms.TextInput(attrs={'readonly':True}),
        }
	
class CallUpdate(UpdateView):
    model = Call
    form_class = CallUpdateForm
    success_url = reverse_lazy('call_list')
    
class CallDelete(DeleteView):
    model = Call
    success_url = reverse_lazy('call_list')
    
class CallEndForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['timestampstart', 'timestampend', 'source', 'destination']
        
        widgets = {
        'source': forms.TextInput(attrs={'readonly':True,}),
        'destination': forms.TextInput(attrs={'readonly':True}),
        'timestampstart': forms.TextInput(attrs={'readonly':True,}),
        'timestampend': forms.TextInput(attrs={'readonly':True, 'value':datetime.datetime.now}),
        }

class CallEnd(UpdateView):
    model = Call
    form_class = CallEndForm
    success_url = reverse_lazy('call_list')

class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all().order_by('source')
    serializer_class = CallSerializer