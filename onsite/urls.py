from rest_framework import routers

from onsite.api import api_views

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'parkinglot', api_views.ParkingLotViewSet, base_name='parkinglot')
router.register(r'finetip', api_views.FineTipViewSet, base_name='finetip')
router.register(r'getusername', api_views.GetUserNameViewSet, base_name='getusername')
router.register(r'getfinetipsuser', api_views.GetFineTipsUserViewSet, base_name='getfinetipsuser')

app_name = 'onsite'
urlpatterns = []
