from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Rafael Vettori', cpf='12345678901',
                    email='rafael.vettori@eventex.com.br', phone='46-9999999999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subsciption_email_to(self):
        expect = ['contato@eventex.com.br', 'rafael.vettori@eventex.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Rafael Vettori', '12345678901', 'rafael.vettori@eventex.com.br', '46-9999999999']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
