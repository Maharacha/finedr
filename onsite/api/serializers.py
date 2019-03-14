from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from drf_extra_fields.fields import Base64ImageField
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
        fields = (
            'url', 'street_name', 'coordinates', 'created_by', 'pub_date')


class FineTipSerializer(serializers.HyperlinkedModelSerializer):
    #created_by_url = serializers.SerializerMethodField()
    #created_by_url = UserSerializer()

    image = Base64ImageField()

    parking_lot_name = serializers.SlugRelatedField(
        source='parking_lot',
        many=False,
        queryset=ParkingLot.objects.all(),
        allow_null=False,
        read_only=False,
        slug_field='street_name'
    )

    created_by_name = serializers.SlugRelatedField(
        source='created_by',
        many=False,
        queryset=User.objects.all(),
        allow_null=False,
        read_only=False,
        slug_field='username'
    )
    
    class Meta:
        model = FineTip
        fields = ('id', 'url', 'image', 'license_plate', 'reason', 'parking_lot_name', 'coordinates', 'pub_date', 'created_by_name')        

    #def create(self, validated_data):
    #    image = validated_data.pop('image')
    #    return FineTip.objects.create(image=image)
