from django.db import IntegrityError
from django.test import TestCase

from mixer.backend.django import mixer

from core.models import Business


class BusinessTestCase(TestCase):
    def setUp(self):
        mixer.cycle(5).blend(Business)

    def test_uniqueness(self):
        business = Business.objects.get(pk=1)
        new_business = Business(name=business.name)
        with self.assertRaises(IntegrityError):
            new_business.save()


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')
