from os import getenv
from dotenv import load_dotenv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Services
from django.views.decorators.csrf import csrf_exempt
import requests

load_dotenv()  # Load environment variables from .env file

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_TOKEN")
TARGET_CHAT_ID = getenv("TARGET_CHAT_ID")

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context)


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        
        telegram_text = (
            f"🔔 **New Contact Form Submission**\n\n"
            f"👤 **Name:** {user_name}\n"
            f"📧 **Email:** {user_email}\n"
            f"💬 **Message:**\n{user_message}"
        )
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TARGET_CHAT_ID,
            "text": telegram_text,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(telegram_url, data=payload, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send Telegram alert: {e}")

        
        return redirect('contact')  # Redirect to the contact page after submission
    return render(request, 'contacts.html')

