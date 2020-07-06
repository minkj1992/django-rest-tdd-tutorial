from rest_framework import serializers
from api.models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Model instance -> JSON"""
    
    class Meta:
        """serializer field와 model field 매핑 메타 클래스"""
        model = Bucketlist
        fields = ('id','name', 'create_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
