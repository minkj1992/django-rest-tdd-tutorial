from rest_framework import generics

from api.serializers import BucketlistSerializer
from api.models import Bucketlist

class CreateView(generics.ListCreateAPIView):
    """get list of bucketlists and post a bucketlist"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """post 데이터 저장"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, DELETE"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer