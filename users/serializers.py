from rest_framework import serializers
from . import models
from users.models import Asset

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )

class AssetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    class Meta:
    	model = Asset
    	fields = ('id', 'asset_type', 'description', 'recipient', 'relation','user')