from django.db import models
from datetime import datetime
class category(models.Model):
    primary_specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.primary_specialization
class sub_category(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name='subcategories')
    sub_specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_specialization

class Doctor_App(models.Model):
      full_name = models.CharField(max_length=255,blank=True,null=True)
      # Doctor_Code = models.CharField(max_length=50, unique=True)
      gender = models.CharField(max_length=20,choices=[('Male', 'Male'),('Female', 'Female'),('Other', 'Other')],blank=True,null=True)
      date_of_birth = models.DateTimeField(blank=True,null=True)
      image = models.ImageField(upload_to="")
      biography_about_doctor = models.TextField(blank=True,null=True)
      category = models.ForeignKey(category, on_delete=models.CASCADE, default=True, null=False)
      sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, default=True, null=False)
      department = models.CharField(max_length=150,blank=True)
      qualifications = models.CharField(max_length=255,choices=[('MBBS','MBBS'),('MD','MD'),('MS','MS'),('DM','DM')],blank=True,null=True)
      years_of_experience = models.IntegerField(blank=True,null=True)
      medical_registration_number = models.CharField(max_length=100,blank=True,null=True)
      medical_council_name = models.CharField(max_length=150,blank=True,null=True)
      official_email = models.EmailField( max_length=255,
    blank=True,
    null=True)
      mobile_number = models.CharField(max_length=15,blank=True,null=True)
      alternate_contact_number = models.CharField(max_length=15,blank=True,null=True)
      consultation_languages = models.CharField(max_length=255,blank=True,null=True)
      emergency_contact = models.CharField(max_length=15, null=True, blank=True)
      employment_type = models.CharField(max_length=30,choices=[('Full-time', 'Full-time'),('Visiting', 'Visiting'),('Consultant', 'Consultant')],blank=True,null=True)
      hospital_clinic_name = models.CharField(max_length=255,blank=True,null=True)
      branch_location = models.CharField(max_length=255,blank=True,null=True)
      room_cabin_number = models.CharField(max_length=50,blank=True,null=True)
      shift_timings = models.CharField(max_length=100,blank=True,null=True)
      on_call_availability = models.BooleanField(default=False,blank=True,null=True)
def __str__(self):
    return self.full_name

