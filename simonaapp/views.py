import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mpesa_api import simulate_transaction
import json

from .generateToken import get_access_token
from .stkPush import initiate_stk_push
from .callback import process_stk_callback

# logger = logging.getLogger(__name__)

# def simulate_transaction_view(request):
#     """Handles the simulation of an M-PESA C2B transaction."""
#     result = None
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         amount = request.POST.get('amount')
        
#         # Trigger the transaction and log the result
#         result = simulate_transaction(amount, phone_number)
#         logger.debug("Transaction Result: %s", result)
    
#     return render(request, 'simulate_transaction.html', {'result': result})

# @csrf_exempt
# def mpesa_confirmation(request):
#     """Handles confirmation callback from Safaricom M-PESA API"""
#     if request.method == 'POST':
#         # Process the confirmation request
#         data = json.loads(request.body)
#         print("Confirmation Data:", data)
#         return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
#     return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid Method"})


# @csrf_exempt
# def mpesa_validation(request):
#     """Handles validation callback from Safaricom M-PESA API"""
#     if request.method == 'POST':
#         # Process the validation request
#         data = json.loads(request.body)
#         print("Validation Data:", data)
#         return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
#     return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid Method"})
