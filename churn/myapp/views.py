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
