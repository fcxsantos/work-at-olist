import datetime, time
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from callapp.serializers import CallSerializer
from callapp.models import Call

class CallList(ListView):
    model = Call
       
class CallBill(ListView):
    model = Call
    my_calls = Call.objects.all()
    template_name = "callapp/call_bill.html"
        
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
        'timestampend': forms.TextInput(attrs={'readonly':True,'value':datetime.datetime.now}),
        }

class CallEnd(UpdateView):
    model = Call
    form_class = CallEndForm
    success_url = reverse_lazy('call_list')

