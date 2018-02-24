from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import HelloWorldView, SubscriberView, Subscriber2View, SubscriberViewSet
from .views import login

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', login),
    url(r'^hello/$', HelloWorldView.as_view(), name="hello_world"),
    url(r'^subscriber/$', SubscriberView.as_view(), name="subscriber"),
    url(r'^subscriber2/$', Subscriber2View.as_view(), name="subscriber2"),
    url(r'^subscriber3/(?P<pk>\d+)/$', SubscriberViewSet.as_view({'get': 'retrieve', 'put':'update'}), name="subscriber3d"),
    url(r'^subscriber3/$', SubscriberViewSet.as_view({'get': 'list', 'post':'create'}), name="subscriber3"),
    ]
