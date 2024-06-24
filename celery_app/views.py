from django.shortcuts import render
from celery import shared_task

# Create your views here.
# your_app/views.py

from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email from Django.'
    from_email = 'nepali.mohan11@gmail.com'
    recipient_list = ['nepalimohan.spices@gmail.com']  # Replace with your recipient email

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully!')
