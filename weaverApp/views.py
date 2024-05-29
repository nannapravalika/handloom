from django.shortcuts import render, redirect, get_object_or_404
from .models import WeaverDetail
from societyMasterApp.models import Society
from masterWeaverApp.models import MasterWeaver

def add_weaver(request):
    societies = Society.objects.all()
    master_weavers = MasterWeaver.objects.all()
    if request.method == 'POST':
        photo = request.FILES.get('photo') 
        weaver_name = request.POST.get('weaver_name')
        society_name = request.POST.get('society_name')
        master_weaver_name = request.POST.get('master_weaver_name')
        weaver_code = request.POST.get('weaver_code')
        weaver_card = request.POST.get('weaver_card')
        ration_card = request.POST.get('ration_card')
        nhdc_passbook = request.POST.get('nhdc_passbook')
        aadhar_card = request.POST.get('aadhar_card')
        bank_name = request.POST.get('bank_name')
        account_no = request.POST.get('account_no')
        ifsc_code = request.POST.get('ifsc_code')
        branch_name = request.POST.get('branch_name')
        age = request.POST.get('age')
        relationship = request.POST.get('relationship')
        address = request.POST.get('address')
        door_no = request.POST.get('door_no')
        street = request.POST.get('street')
        area_name = request.POST.get('area_name')
        mandal = request.POST.get('mandal')
        district = request.POST.get('district')
        state = request.POST.get('state')
        mobile_no = request.POST.get('mobile_no')
        payment = request.POST.get('payment')
        date = request.POST.get('date')
        signature = request.POST.get('signature')
        no_of_charkas = request.POST.get('no_of_charkas')
        no_of_looms = request.POST.get('no_of_looms')
        
        WeaverDetail.objects.create(
            photo=photo,
            weaver_name=weaver_name,
            society_name=society_name,
            master_weaver_name=master_weaver_name,
            weaver_code=weaver_code,
            weaver_card=weaver_card,
            ration_card=ration_card,
            nhdc_passbook=nhdc_passbook,
            aadhar_card=aadhar_card,
            bank_name=bank_name,
            account_no=account_no,
            ifsc_code=ifsc_code,
            branch_name=branch_name,
            age=age,
            relationship=relationship,
            address=address,
            door_no=door_no,
            street=street,
            area_name=area_name,
            mandal=mandal,
            district=district,
            state=state,
            mobile_no=mobile_no,
            payment=payment,
            date=date,
            signature=signature,
            no_of_charkas=no_of_charkas,
            no_of_looms=no_of_looms,
        )
        
        return redirect('list_weavers')
    return render(request, 'weaver/add_weaver.html', {'societies': societies , 'master_weavers':master_weavers})

def edit_weaver(request, id):
    societies = Society.objects.all()
    master_weavers = MasterWeaver.objects.all()
    weaver = get_object_or_404(WeaverDetail, pk=id)
    if request.method == 'POST':
        weaver.photo = request.FILES.get('photo') 
        weaver.weaver_name = request.POST.get('weaver_name')
        weaver.society_name = request.POST.get('society_name')
        weaver.master_weaver_name = request.POST.get('master_weaver_name')
        weaver.weaver_code = request.POST.get('weaver_code')
        weaver.weaver_card = request.POST.get('weaver_card')
        weaver.ration_card = request.POST.get('ration_card')
        weaver.nhdc_passbook = request.POST.get('nhdc_passbook')
        weaver.aadhar_card = request.POST.get('aadhar_card')
        weaver.bank_name = request.POST.get('bank_name')
        weaver.account_no = request.POST.get('account_no')
        weaver.ifsc_code = request.POST.get('ifsc_code')
        weaver.branch_name = request.POST.get('branch_name')
        weaver.age = request.POST.get('age')
        weaver.relationship = request.POST.get('relationship')
        weaver.address = request.POST.get('address')
        weaver.door_no = request.POST.get('door_no')
        weaver.street = request.POST.get('street')
        weaver.area_name = request.POST.get('area_name')
        weaver.mandal = request.POST.get('mandal')
        weaver.district = request.POST.get('district')
        weaver.state = request.POST.get('state')
        weaver.mobile_no = request.POST.get('mobile_no')
        weaver.payment = request.POST.get('payment')
        weaver.date = request.POST.get('date')
        weaver.signature = request.POST.get('signature')
        weaver.no_of_charkas = request.POST.get('no_of_charkas')
        weaver.no_of_looms = request.POST.get('no_of_looms')
       
        weaver.save()
        return redirect('list_weavers')
    return render(request, 'weaver/edit_weaver.html', {'weaver': weaver,'societies': societies , 'master_weavers':master_weavers})

def list_weavers(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        weavers = WeaverDetail.objects.filter(weaver_name__icontains=search_query,is_deleted=False)
        # weavers = WeaverDetail.objects.filter(weaver_name__icontains=search_query)
        
    else:
        weavers = WeaverDetail.objects.filter(is_deleted=False)
        # weavers = WeaverDetail.objects.all()
    return render(request, 'weaver/list_weaver.html', {'weavers': weavers, 'search_query': search_query})

def remove_weaver(request, id):
    weaver = get_object_or_404(WeaverDetail, id=id)
    weaver.is_deleted = True  # Mark as deleted
    weaver.save()
    return redirect('list_weavers')

def remove_weaver(request, id):
    weaver = get_object_or_404(WeaverDetail, pk=id)
    weaver.is_deleted = True
    weaver.save()
    return redirect('list_weavers')
