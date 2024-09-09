from django.urls import path
from .views import create_model_view, test_thread_view, test_transaction_view, rectangle_view

urlpatterns = [
    path('create/', create_model_view),
    path('test-thread/', test_thread_view),
    path('test-transaction/', test_transaction_view),

    path('test-rectangle/', rectangle_view),
]
