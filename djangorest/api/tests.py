from django.test import TestCase
from api.models import Bucketlist

class ModelTestCase(TestCase):
    """이 클래스는 bucketlist 모델을 위한 test suite를 정의합니다."""

    def setUp(self):
        """테스트 클라이언트와 기타 테스트 변수를 정의합니다."""
        self.bucketlist_name = "Netflix Google NASA kakao naver"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)
    
    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()

        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
    