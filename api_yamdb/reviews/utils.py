import random
import string

from django.conf import settings
from django.core.mail import send_mail


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject='Регистрация на Yamdb, код подтверждения',
        message='Спасибо за регистрацию в нашем сервисе. '
                f'Код подтверждения: {confirmation_code}',
        from_email='register@yambd.com',
        recipient_list=[email],
        fail_silently=False,
    )


def generate_confirmation_code():
    return ''.join(
        random.choice(
            string.ascii_uppercase + string.digits,
        ) for n in range(settings.SIZE_CODE)
    )
