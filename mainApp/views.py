from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from weaverApp.models import WeaverDetail
from .models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not email or not password:
            return HttpResponse("Email or Password is empty!")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid email or password.")

    return render(request, 'login.html')
 
def index(request):
    weavers_count = WeaverDetail.objects.count()
    # invoices_count = Invoice.objects.count()  # Assuming there's an Invoice model as well
   # indents_count = Indent.objects.count()
   # reports_count = Report.objects.count()  # Assuming there's a Report model

    context = {
        'weavers_count': weavers_count,
        # 'invoices_count': invoices_count,
        #'indents_count': indents_count,
        #'reports_count': reports_count,
    }
    
    return render(request, 'index.html', context)
