from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.urls import reverse

from api.models import Bucketlist


class BucketlistCreateTestCase(APITestCase):
    """이 클래스는 bucketlist 모델을 위한 test suite를 정의합니다."""
    def setUp(self):
        self.name = "Be a Kakao developer"
        self.data = {'name': self.name}
        self.url = reverse('bucketlist-list')
        
    def test_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()

        response = self.client.post(self.url, self.data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bucketlist.objects.count(), old_count + 1)
        self.assertEqual(Bucketlist.objects.get().name, self.data["name"])


# https://github.com/erdem/DRF-TDD-example/blob/master/todoapp/todos/tests.py
class BucketlistDetailTestCase(APITestCase):
    def setUp(self):
        self.name = "Be a Kakao developer"
        self.bucketlist = Bucketlist.objects.create(name=self.name)
        self.url = reverse('bucketlist-detail', kwargs={"pk": self.bucketlist.pk})

    def test_get_a_bucketlist(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.name, response.data['name'])

