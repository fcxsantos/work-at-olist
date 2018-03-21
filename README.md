Description
-----------
This application provides the users to manage telephone calls made from a source phone number to a destination phone number. 

Call List
---------
The link https://callappfcxsantos.herokuapp.com/callapp/ provides users with a page that can be used to list all the calls with the next columns<br>
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


Work environment used to run this project 
-----------------------------------------
The next requirements were use in this project:<br>
python-3.6.4 - environment to use Python language<br>
python-dateutil 2.7.0 - module to manipulate datetime objects<br>
Django 2.0.3 - Python-based framework for building web applications<br>
djangorestframework 3.7.7 - toolkit for building Web APIs REST in Django projects<br>
pytz 2018.3 - World Timezone Definitions for Python<br>
whitenoise 3.3.1 - makes a web app a self-contained unit that can be deployed anywhere<br>
gunicorn 19.7 - a Python Web Server Gateway Interface (WSGI) HTTP server<br>
