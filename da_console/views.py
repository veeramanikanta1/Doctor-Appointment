from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm
from django.http import JsonResponse
from . models import Doctor_App,category,sub_category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def show_all_docs(request):
    doctors = Doctor_App.objects.all()
    page_num = request.GET.get('page')  # Creating the Total Page
    paginator = Paginator(doctors, 3)  # Setting total number of products in a page : 3

    try:
        doctors = paginator.page(page_num)  #
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)

    context = {
        'doctors':doctors
    }
    return render(request,'showdoctors.html',context)

def doc_details(request,pk):
    doctor = Doctor_App.objects.get(id=pk)
    context = {
        'doctor':doctor
    }
    return render(request,'doctor_details.html',context)

def add_doctor(request):
    form=DoctorForm()
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_all_docs')
    return render(request,'add_forms.html',{'form':form})

def update_doctor(request,pk):
    doctor = Doctor_App.objects.get(id=pk)
    form=DoctorForm(instance=doctor)
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('show_all_docs')
    return render(request,'update_details.html',{'form':form})


def delete_doctor(request,pk):
    doctor = Doctor_App.objects.get(id=pk)
    doctor.delete()
    return redirect('show_all_docs')

# @login_required(login_url='accounts/login')
def doctor_list(request):
    doctor=Doctor_App.objects.all()
    categories = category.objects.all()
    subcategories = sub_category.objects.all()
    return render(request,'doctor_list.html',{'doctor':doctor,'categories': categories,
        'subcategories': subcategories})

@login_required(login_url='accounts/login')
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor_App, id=id)

    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')

    return redirect('doctor_list')

@login_required(login_url='accounts/login')
def doctor_delete1(request):
    id= request.session.get('id')
    x=Doctor_App.objects.get(id=id)
    if x:
        x.delete()
        return redirect("doctor_list")
    return render(request,"doctor_list.html")


from django.http import JsonResponse

@login_required(login_url='accounts/login')
def doctorDetailsJson(request, pk):
    doctor = get_object_or_404(Doctor_App, id=pk)
    data = {
        'id': doctor.id,
        'Employee_id': doctor.id,
        'full_name': doctor.full_name,
        'gender': doctor.gender,
        'date_of_birth': doctor.date_of_birth.strftime('%b. %d, %Y') if doctor.date_of_birth else '',
        'About_doctor': doctor.biography_about_doctor,
        'primary_specialization': doctor.category.primary_specialization if doctor.category else '',
        'sub_specialization': doctor.sub_category.sub_specialization if doctor.sub_category else '',
        'department': doctor.department,
        'qualification_options': doctor.qualifications,
        'years_of_experience': doctor.years_of_experience,
        'medical_registration_number': doctor.medical_registration_number,
        'medical_council_name': doctor.medical_council_name,
        'official_email': doctor.official_email,
        'mobile_number': doctor.mobile_number,
        'alternate_number': doctor.alternate_contact_number,
        'consultation_languages': doctor.consultation_languages,
        'emergency_contact_number': doctor.emergency_contact,
        'Employment_type': doctor.employment_type,
        'hospital_name': doctor.hospital_clinic_name,
        'location': doctor.branch_location,
        'Room_number': doctor.room_cabin_number,
        'shift_timings': doctor.shift_timings,
        'on_call_availability': doctor.on_call_availability,
        'profile_image': doctor.image.url if doctor.image else '',
    }
    return JsonResponse(data)


@login_required(login_url='accounts/login')
def add_doctors(request):
    form=DoctorForm()
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    return render(request,'add_forms.html',{'form':form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor_App
from datetime import datetime

@login_required(login_url='accounts/login')
def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor_App, id=id)

    if request.method == 'POST':
        try:

            # Basic Information
            doctor.full_name = request.POST.get('full_name')
            doctor.gender = request.POST.get('gender')
            doctor.date_of_birth = request.POST.get('date_of_birth') or None
            doctor.biography_about_doctor = request.POST.get('biography_about_doctor') or ''

            # Professional Information
            doctor.primary_specialization = request.POST.get('primary_specialization')
            doctor.sub_specializations = request.POST.get('sub_specializations') or ''
            doctor.department = request.POST.get('department')
            doctor.qualifications = request.POST.get('qualifications')
            doctor.years_of_experience = request.POST.get('years_of_experience') or None
            doctor.medical_registration_number = request.POST.get('medical_registration_number') or ''
            doctor.medical_council_name = request.POST.get('medical_council_name')

            # Contact Information
            doctor.official_email = request.POST.get('official_email')
            doctor.mobile_number = request.POST.get('mobile_number') or ''
            doctor.alternate_contact_number = request.POST.get('alternate_contact_number') or ''
            doctor.consultation_languages = request.POST.get('consultation_languages')
            doctor.emergency_contact = request.POST.get('emergency_contact') or ''

            # Work Information
            doctor.employment_type = request.POST.get('employment_type')
            doctor.hospital_clinic_name = request.POST.get('hospital_clinic_name')
            doctor.branch_location = request.POST.get('branch_location') or ''
            doctor.room_cabin_number = request.POST.get('room_cabin_number') or ''
            doctor.shift_timings = request.POST.get('shift_timings')

            # On Call Availability
            on_call = request.POST.get('on_call_availability')
            doctor.on_call_availability = (on_call == 'True' or on_call == 'true')

            # Image Upload
            if 'image' in request.FILES:
                if doctor.image:
                    doctor.image.delete()
                doctor.image = request.FILES['image']
            doctor.save()
            # messages.success(request, 'Doctor added successfully!')
            return redirect('doctor_list')
        except Exception as e:
            messages.error(request, f'Error adding doctor: {str(e)}')
        return redirect('doctor_list')
    return redirect('doctor_list')

@login_required(login_url='accounts/login')
def searchBar(request):
    if request.method == 'GET':  # get = Get => True
        query = request.GET.get('query')  # query = 999, ABC, ABC99, ABC99$#$#
        if query:  # True
            docs = Doctor_App.objects.filter(full_name__icontains=query)  # 999 = 4 records found
            return render(request, 'searchbar.html', {"docs": docs})
        else:
            print("No Products Found to show in the Database")
            return render(request, 'searchbar.html', {})
