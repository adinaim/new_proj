from django.conf import settings

def send_activation_sms(phone, activation_code):
    from twilio.rest import Client
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Это ваш активационный код {activation_code} Adinai',
        from_=settings.TWILIO_NUMBER,
        to=phone
    )
    print(message.sid)