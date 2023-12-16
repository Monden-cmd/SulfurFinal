from django.conf import settings
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tour.sulfur.models import Tour


@pytest.mark.django_db
class TourListCreateViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('tour-list-create')
        self.data = {'place': 'Test Place', 'date': '2023-01-01', 'price': 100, 'transport': 'Test Transport'}

    def test_create_tour(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tour.objects.count(), 1)
        self.assertEqual(Tour.objects.get().place, 'Test Place')

    def test_list_tours(self):
        Tour.objects.create(place='Tour 1', date='2023-02-01', price=200, transport='Transport 1')
        Tour.objects.create(place='Tour 2', date='2023-03-01', price=300, transport='Transport 2')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
