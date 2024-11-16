from django.urls import path
from . import views

urlpatterns = [
    path('api/simona/confirmation', views.mpesa_confirmation, name='mpesa_confirmation'),
    path('api/simona/validation', views.mpesa_validation, name='mpesa_validation'),
    path('simulate-transaction/', views.simulate_transaction_view, name='simulate_transaction'),
]
