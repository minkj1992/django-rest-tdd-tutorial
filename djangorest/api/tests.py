from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.urls import reverse

from api.models import Bucketlist


class BucketlistTestCase(APITestCase):
    """이 클래스는 bucketlist 모델을 위한 test suite를 정의합니다."""

    def test_create_a_bucketlist(self):
        url = reverse('create')
        name = "Be a Kakao developer"
        data = {'name': name}
        old_count = Bucketlist.objects.count()

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bucketlist.objects.count(), old_count + 1)
        self.assertEqual(Bucketlist.objects.get().name, name)
