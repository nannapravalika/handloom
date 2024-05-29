from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from mainApp.views import index
from .models import Society
from django.core.paginator import Paginator

@csrf_exempt
def create_society(request):
    if request.method == 'POST':
        society_name = request.POST.get('society_name', '')
        address = request.POST.get('address', '')
        door_no = request.POST.get('door_no', '')
        street = request.POST.get('street', '')
        area_name = request.POST.get('area_name', '')
        mandal = request.POST.get('mandal', '')
        district = request.POST.get('district', '')
        state = request.POST.get('state', '')
        mobile_no = request.POST.get('mobile_no', '')
        status = request.POST.get('status', '')

        society= Society.objects.create(society_name=society_name , address=address, door_no=door_no, street=street, area_name=area_name, mandal=mandal, district=district, state=state, mobile_no=mobile_no, status=status)
            
        return redirect('list_society')  # Redirect to a success page or any other page

    return render(request, 'society/add_society.html')

def edit_society(request, id):
   
    societies = get_object_or_404(Society, pk=id)
    if request.method == 'POST':
        societies.society_name = request.POST.get('society_name', '')
        societies.address = request.POST.get('address', '')
        societies.door_no = request.POST.get('door_no', '')
        societies.street = request.POST.get('street', '')
        societies.area_name = request.POST.get('area_name', '')
        societies.mandal = request.POST.get('mandal', '')
        societies.district = request.POST.get('district', '')
        societies.state = request.POST.get('state', '')
        societies.mobile_no = request.POST.get('mobile_no', '')
        societies.status = request.POST.get('status', '')
       
        societies.save()
        return redirect('list_society')
    return render(request, 'society/edit_society.html', {'society': societies})



def list_society(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        societies = Society.objects.filter(society_name__icontains=search_query, is_deleted=False)
    else:
        societies = Society.objects.filter(is_deleted=False)

    return render(request, 'society/list_society.html', {'societies': societies})


 

def delete_society(request, id):
    society = get_object_or_404(Society, id=id)
    society.is_deleted = True  # Mark as deleted
    society.save()
    return redirect('list_society')

