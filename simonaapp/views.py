from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def mpesa_confirmation(request):
    """Handles confirmation callback from Safaricom M-PESA API"""
    if request.method == 'POST':
        # Process the confirmation request
        data = json.loads(request.body)
        print("Confirmation Data:", data)
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid Method"})


@csrf_exempt
def mpesa_validation(request):
    """Handles validation callback from Safaricom M-PESA API"""
    if request.method == 'POST':
        # Process the validation request
        data = json.loads(request.body)
        print("Validation Data:", data)
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid Method"})
