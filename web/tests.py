"""
from django.test import TestCase

from .views import send_test_email
from django.core import mail

class EmailTest(TestCase):
    def test_send_email(self):
        send_test_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Assunto do E-mail')
"""

from django.test import TestCase, override_settings
from django.conf import settings
from django.core.mail import send_mail

def send_test_email():
    send_mail(
        'Assunto de teste do E-mail',
        'Mensagem de teste do e-mail',
        'jadsom2000hotmail@gmail.com',  # Email de origem
        ['jadson.g-matos@outlook.com'],  # Lista de emails de destino
        fail_silently=False,
    )


class RealEmailTest(TestCase):
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_send_real_email(self):
        send_test_email()
