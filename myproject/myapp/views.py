import threading
from django.http import HttpResponse, JsonResponse
from .models import TestModel
from django.db import transaction
from .rectangle import Rectangle

def create_model_view(request):
    obj = TestModel.objects.create(name="Test Name")
    return HttpResponse("Model created. Check terminal for signal execution.")


def test_thread_view(request):
    print(f"View thread: {threading.current_thread().name}")
    obj = TestModel.objects.create(name="Thread Test")
    return HttpResponse("Thread test completed.")

def test_transaction_view(request):
    try:
        with transaction.atomic():
            obj = TestModel.objects.create(name="Transaction Test")
            raise Exception("Intentional Error to test transaction rollback")
    except Exception as e:
        return HttpResponse(f"Transaction rolled back: {str(e)}")
    
def rectangle_view(request):
    rectangle = Rectangle(length=10, width=5)
    result = list(rectangle)  # Iterate over the instance
    return JsonResponse({'rectangle': result})