from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.views import APIView
from onsite.serializers import UserSerializer, GroupSerializer, ParkingLotSerializer, FineTipSerializer
from onsite.models import ParkingLot, FineTip
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    # def destroy(self, request, *args, **kwargs):
    #     if "admin" in groups:
    #         return Response({"address": request.data.get("name") + "deleted."}, status=status.HTTP_202_ACCEPTED)
    #     else:
    #         return Response({"error": "permission denied"}, status=status.HTTP_403_FORBIDDEN)


class FineTipViewSet(viewsets.ModelViewSet):
    queryset = FineTip.objects.all()
    serializer_class = FineTipSerializer
    
    
# class LoginView(CreateAPIView):            
#     permission_classes = ()
#     serializer_class = UserSerializer

#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         print(username)
#         print(password)
#         serialized = UserSerializer(data=request.data)
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
