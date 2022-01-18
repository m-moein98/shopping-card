from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestSetUp(APITestCase):
    def setUp(self):
        self.end_points = {
            'card': reverse('card'),
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
