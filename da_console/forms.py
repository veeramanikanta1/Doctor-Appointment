from django import forms
from .models import Doctor_App,category,sub_category

class categoryform(forms.ModelForm):
        class Meta:
            model = category
            fields = '__all__'
            widgets = {
                'primary_specialization': forms.TextInput(attrs={'class': 'form-control'})
            }

class subcategoryForm(forms.ModelForm):
        class Meta:
            model = sub_category
            fields = '__all__'
            widgets = {
                'category': forms.Select(attrs={'class': 'form-control'}),
                'sub_specialization': forms.TextInput(attrs={'class': 'form-control'})
            }
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor_App
        fields=['full_name','image','biography_about_doctor','category','mobile_number','date_of_birth','gender',
                'sub_category','department','qualifications','years_of_experience','medical_registration_number','medical_council_name',
                'alternate_contact_number','official_email','consultation_languages','emergency_contact','employment_type','hospital_clinic_name',
                'branch_location','room_cabin_number','shift_timings','on_call_availability']
        widgets = { 'full_name': forms.TextInput(attrs={'class':'form-control'}),
                    'category': forms.Select(attrs={'class': 'form-control'}),
                    'biography_about_doctor': forms.TextInput(attrs={'class':'form-control'}),
                    'mobile_number': forms.TextInput(attrs={'class':'form-control'}),
                    'image': forms.FileInput(attrs={'class':'form-control'}),
                    'date_of_birth': forms.DateInput(attrs={'class':'form-control'}),
                    'gender': forms.TextInput(attrs={'class':'form-control'}),
                    'sub_category': forms.Select(attrs={'class':'form-control'}),
                    'department': forms.TextInput(attrs={'class':'form-control'}),
                    'qualifications': forms.TextInput(attrs={'class':'form-control'}),
                    'years_of_experience': forms.TextInput(attrs={'class':'form-control'}),
                    'medical_registration_number': forms.TextInput(attrs={'class':'form-control'}),
                    'medical_council_name': forms.TextInput(attrs={'class':'form-control'}),
                    'official_email': forms.EmailInput(attrs={'class':'form-control'}),
                    'consultation_languages': forms.TextInput(attrs={'class':'form-control'}),
                    'alternate_contact_number': forms.TextInput(attrs={'class':'form-control'}),
                    'emergency_contact': forms.TextInput(attrs={'class':'form-control'}),
                    'employment_type': forms.TextInput(attrs={'class':'form-control'}),
                    'hospital_clinic_name': forms.TextInput(attrs={'class':'form-control'}),
                    'branch_location': forms.TextInput(attrs={'class':'form-control'}),
                    'room_cabin_number': forms.TextInput(attrs={'class':'form-control'}),
                    'shift_timings': forms.TextInput(attrs={'class':'form-control'}),
                    'on_call_availability': forms.TextInput(attrs={'class':'form-control'}),}