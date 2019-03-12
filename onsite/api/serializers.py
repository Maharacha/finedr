from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer

from onsite.models import (ParkingLot, FineTip)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'


class FineTipSerializer(serializers.HyperlinkedModelSerializer):
    #created_by_url = serializers.SerializerMethodField()
    #created_by_url = UserSerializer()

    class Meta:
        model = FineTip
        #fields = ('url', 'license_plate', 'reason', 'street_name', 'coordinates', 'pub_date')        
        fields = '__all__'
        
    #def get_created_by_url(self, validated_data):
      #  print(validated_data.created_by)
        #created_by_id = User.objects.get(username=validated_data.created_by).id
        #print(created_by_url_id)
        #created_by_url = 
        #return created_by_url
