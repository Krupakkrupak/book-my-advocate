from django.urls import path
from . import views

urlpatterns = [
    # Advocate endpoints
    path('advocates/', views.AdvocateListCreate.as_view(), name='advocate-list-create'),
    path('advocates/<int:pk>/', views.AdvocateRetrieveUpdateDestroy.as_view(), name='advocate-detail'),
    
    # Case endpoints
    path('cases/', views.CaseListCreate.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', views.CaseRetrieveUpdateDestroy.as_view(), name='case-detail'),
    
    # Analytics endpoints
    path('advocates/success-rate/', views.AdvocateSuccessRateAPI.as_view(), name='advocate-success-rate'),
    path('dashboard/success-rate/', views.ClientDashboardSuccessRateAPI.as_view(), name='client-dashboard-success-rate'),
]
