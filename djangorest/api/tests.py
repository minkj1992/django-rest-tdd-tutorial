from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

from api.models import Bucketlist


class ModelTestCase(TestCase):
    """이 클래스는 bucketlist 모델을 위한 test suite를 정의합니다."""

    def setUp(self):
        """테스트 클라이언트와 기타 테스트 변수를 정의합니다."""
        self.bucketlist_name = "Be a Kakao developer"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)
    
    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()

        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
    

class ViewTestCase(TestCase):
    """api view Test suite"""

    def setUp(self):
        """테스트 클라이언트와 테스트 변수를 정의합니다."""
        self.client = APIClient
        self.bucketlist_data = {'name': "Go to USA"}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json',
            )
        
    def test_api_view_can_create_a_bucketlist(self):
        """api view에 버킷 생성 기능이 있는지 테스트합니다."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

