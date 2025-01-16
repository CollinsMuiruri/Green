from django.urls import path
from . import views

urlpatterns = [
    # path('api/simona/confirmation', views.mpesa_confirmation, name='mpesa_confirmation'),
    # path('api/simona/validation', views.mpesa_validation, name='mpesa_validation'),
    # path('simulate-transaction/', views.simulate_transaction_view, name='simulate_transaction'),

    path('accesstoken/', views.get_access_token, name='get_access_token'),
    path('stkpush/', views.initiate_stk_push, name='initiate_stk_push'),
    path('callback/', views.process_stk_callback, name='process_stk_callback'),
]
