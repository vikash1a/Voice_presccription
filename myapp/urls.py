from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('signup/', views.signup,name='signup'),
]
urlpatterns += [
    path('doctor/', views.doctorprofile.as_view(), name='doctor-profile'),
    path('doctor/prescription/<uuid:pk>', views.prescriptionDetailView.as_view(), name='prescription-detail'),
]

urlpatterns += [  
    path('doctor/prescription/create/', views.prescriptionCreate.as_view(), name='prescription_create'),
    path('doctor/prescription/<uuid:pk>/update/', views.prescriptionUpdate.as_view(), name='prescription_update'),
    path('doctor/prescription/<uuid:pk>/delete/', views.prescriptionDelete.as_view(), name='prescription_delete'),
]
