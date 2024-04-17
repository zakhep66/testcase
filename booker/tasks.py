import os

from dotenv import load_dotenv
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


load_dotenv()


@shared_task
def send_email_task(book_title):
    users = User.objects.all().filter(email__isnull=False)
    subject = "Новая книга добавлена!"
    message = f'Привет! Мы только что добавили новую книгу "{book_title}". Проверьте наш сайт для подробностей.'
    sender_email = os.getenv("EMAIL_HOST_USER")
    for user in users:
        send_mail(subject, message, sender_email, [user.email])
