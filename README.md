# Ex.03 Design a Website for Server Side Processing
## Date:14-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
churn.html:

<html>
    <head>
        <title>WEB EXERCISE 3</title>
    </head>
    <body>
        <h1 align="center">CHURN RATE CALCULATING</h1>
        <h2 align="center">GOKUL K</h2>
        <h3 align="center">26017366</h3>
            <form method="POST">
                {%csrf_token%}
            <label>Customer lost:</label>
        <input type="number" name="customer_lost" value="{{cl}}">
            <br></br>
            <label>Initial customer:</label>
        <input type="number" name="initial_customer" value="{{ic}}">
            <br></br>
        <input type="submit" value="calculate">
            <br></br>
            <label>Churn rate:</label>
        <input type="number" value="{{rate}}">
            </form>
    </body>
</html>

views.py:

from django.shortcuts import render

def churn_rate(request):
    cl = float(request.POST.get('customer_lost', '0'))
    ic = float(request.POST.get('initial_customer', '0'))

    rate = cl * ic if request.method == 'POST' else 0

    print("Customer lost =", cl)
    print("Initial customer =", ic)
    print("Churn rate  =", rate)

    return render(
        request,
        'myapp/churn.html',
        {'cl': cl, 'ic': ic, 'rate': rate}
    )

urls.py:

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.churn_rate, name='churn_rate'),
]

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-14 131546.png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-11-14 131434.png>)


## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
