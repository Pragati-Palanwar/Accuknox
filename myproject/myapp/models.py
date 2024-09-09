from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time, threading

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5)
    print("Signal handler finished.")

@receiver(post_save, sender=TestModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

@receiver(post_save, sender=TestModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print("Signal executed inside transaction.")
