from django.urls import path
from . import views
urlpatterns=[
    path('',views.show_all_docs,name='show_all_docs'),
    path('appointment/<int:pk>',views.doc_details,name='doctor'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('update/<int:pk>/',views.update_doctor,name='update'),
    path('delete/<int:pk>/',views.delete_doctor,name='delete'),
    path('doctor_list/',views.doctor_list,name="doctor_list"),
    path('doctor_delete/<int:id>/',views.doctor_delete,name="doctor_delete"),
    path('doctor_delete1/',views.doctor_delete1,name="doctor_delete1"),
    path('edit/<int:id>/', views.edit_doctor, name='edit'),
    path('doctor-details-json/<int:pk>/', views.doctorDetailsJson, name='doctorDetailsJson'),
    path('add_doctors/', views.add_doctors, name='add_doctors'),
    path('search/',views.searchBar,name='search'),

]
