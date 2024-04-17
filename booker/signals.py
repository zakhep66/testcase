from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

from .tasks import send_email_task


@receiver(post_save, sender=Book)
def notify_users_about_new_book(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(instance.title)
