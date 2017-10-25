from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class TestApp(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
