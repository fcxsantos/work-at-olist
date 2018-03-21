Description
-----------
This application is used to manage telephone calls made from a source phone number to a destination phone number. 

Call List
---------
The link https://callappfcxsantos.herokuapp.com/callapp/calls lists all the calls in JSON notation to demonstrate that HTTP REST API is used in the project<br>
The link https://callappfcxsantos.herokuapp.com/callapp/ also provides users with a HTML page that can be used to list all the calls with the next columns<br>
Id - call id that is generated sequentially<br>
Start - call start date and time<br>
End - call end date and time<br>
Source - phone number that originates the call<br>
Destination - phone number that receives the call<br>
The next functions are also showed:<br>
Add a call - includes a new call<br>
Telephone bill - lists calls and prices for a phone number by period<br>
Update - updates a call<br>
Delete - deletes a call<br>
End - ends a call<br>

Add a call
----------
This page shows the next fields to include a new call:<br>
Start - call start date and time; this field is read only and is filled with current date and time<br>
End - call end date and time; this field is empty<br> 
Source - phone number that originates the call<br>
Destination - phone number that receives the call<br>

Update
------
This page shows the same fields listed in <b>Add a call</b> and can be used to update a call<br>
Start - call start date and time; this field is read only<br>
End - call end date and time; this field is read only<br> 
Source - phone number that originates the call<br>
Destination - phone number that receives the call<br>

Delete
------
Deletes a call; a confirmation message is showed before the delete operation<br>

End
---
This page shows the same fields listed in <b>Add a call</b> and can be used to end a call<br>
Start - call start date and time; this field is read only<br> 
End - call end date and time; this field is read only and is filled with current date and time<br> 
Source - phone number that originates the call; this field is read only<br> 
Destination - phone number that receives the call; this field is read only<br> 

Telephone bill
--------------
This page shows all the calls for a given phone number by period with the next columns<br>
Id - call id that is generated sequentially<br>
Start - call start date and time<br>
End - call end date and time<br>
Source - phone number that originates the call<br>
Destination - phone number that receives the call<br>
Duration - duration between start and end call<br>
Price - price calculated for the call; the last row shows a total for the listed calls<br>
The next fields are also showed:<br>
Phone - phone number that can be used to filter calls made from a source phone number<br>
Period - month and year that can be used to filter calls that were finished in the same month and year<br>

Installing and testing instructions
-----------------------------------
Python setup download from https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe
pip install python-dateutil - installs dateutil module<br>
pip install django - installs Django framework<br>
pip install djangorestframework - installs Django REST framework<br>
pip install pytz - install pytz<br>
pip install gunicorn - installs gunicorn <br>
pip install whitenoise - installs whitenoise<br>
django-admin.py startproject callproj - creates the project<br>
cd callproj - changes the current directory to callproj<br>
django-admin.py startapp callapp - creates the application<br>
python manage.py runserver - starts the service<br>

Work environment used to run this project 
-----------------------------------------
The next requirements were use in this project:<br>
PC with an Intel i5 processor, RAM memory with 8GB, HD SATA with 1TB, Windows 10 as SO and TextPad as text editor
python-3.6.4 - environment to use Python language<br>
python-dateutil 2.7.0 - module to manipulate datetime objects<br>
Django 2.0.3 - Python-based framework for building web applications<br>
djangorestframework 3.7.7 - toolkit for building Web APIs REST in Django projects<br>
pytz 2018.3 - World Timezone Definitions for Python<br>
whitenoise 3.3.1 - makes a web app a self-contained unit that can be deployed anywhere<br>
gunicorn 19.7 - a Python Web Server Gateway Interface (WSGI) HTTP server<br>

API documentation
-----------------
callapp/models.py - defines a Call class<br>
callapp/serializers.py - defines fields to be showed in JSON notation<br>
callapp/urls.py - defines the urls for the application<br>
callapp/views.py - defines information that are presented to users<br>
callapp/templates/call_bill.html - lists calls filtered by phone and period<br>
callapp/templates/call_confirm_delete.html - shows a message to confirm deletion<br>
callapp/templates/call_form.html - form that is used to include, update or end a call<br>
callapp/templates/call_list.html - lists all the calls<br>