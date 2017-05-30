from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
