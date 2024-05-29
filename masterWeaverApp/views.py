from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models import MasterWeaver
from django.core.paginator import Paginator
from django.contrib import messages
from .models import MasterWeaver

def add_master_weaver(request):
    if request.method == 'POST':
        master_weaver_name = request.POST.get('master_weaver_name', '')
        address = request.POST.get('address', '')
        door_no = request.POST.get('door_no', '')
        street = request.POST.get('street', '')
        area_name = request.POST.get('area_name', '')
        mandal = request.POST.get('mandal', '')
        district = request.POST.get('district', '')
        state = request.POST.get('state', '')
        mobile_no = request.POST.get('mobile_no', '')
        status = 0
        
        # if MasterWeaver.objects.filter(area_name=area_name).exists():
        #     messages.error (request, "Master Weaver already exist")
        # else:
        #     MasterWeaver.objects.create(master_weaver_name=master_weaver_name,
        #     address=address,
        #     door_no=door_no,
        #     street= street,
        #     area_name=area_name,
        #     mandal=mandal,
        #     district=district,
        #     state=state,
        #     mobile_no=mobile_no,
        #     status=status,)
        #     messages.success(request, "Account created successful")
        
        master_weaver = MasterWeaver.objects.create(
            master_weaver_name=master_weaver_name,
            address=address,
            door_no=door_no,
            street= street,
            area_name=area_name,
            mandal=mandal,
            district=district,
            state=state,
            mobile_no=mobile_no,
            status=status,
            
        )
        master_weaver.save()
        return redirect('list_master_weaver')
    
    return render(request, 'masterWeaver/add_master_weaver.html')

def edit_master_weaver(request, id):
       
    master_weaver = get_object_or_404(MasterWeaver, pk=id)
    if request.method == 'POST':
        master_weaver.master_weaver_name = request.POST.get('master_weaver_name', '')
        master_weaver.address = request.POST.get('address', '')
        master_weaver.door_no = request.POST.get('door_no', '')
        master_weaver.street = request.POST.get('street', '')
        master_weaver.area_name = request.POST.get('area_name', '')
        master_weaver.mandal = request.POST.get('mandal', '')
        master_weaver.district = request.POST.get('district', '')
        master_weaver.state = request.POST.get('state', '')
        master_weaver.mobile_no = request.POST.get('mobile_no', '')
        master_weaver.status = 0
       
        master_weaver.save()
        return redirect('list_master_weaver')
    return render(request, 'masterWeaver/edit_master_weaver.html', {'master_weaver': master_weaver})





def list_master_weaver(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        master_weaver_list = MasterWeaver.objects.filter(master_weaver_name__icontains=search_query,is_deleted=False)
        # master_weaver_list = MasterWeaver.objects.filter(master_weaver_name__icontains=search_query)
        
    else:
        master_weaver_list = MasterWeaver.objects.filter(is_deleted=False)
        # master_weaver_list = MasterWeaver.objects.all()

    return render(request, 'masterWeaver\list_master_weaver.html', {"master_weaver_list":master_weaver_list})


def delete_master_weaver(request, id):
    # Change status to inactive (delete)
    master_weaver = get_object_or_404(MasterWeaver, pk=id)
    master_weaver.is_deleted = True
    master_weaver.save()
    return redirect('list_weavers')
     
