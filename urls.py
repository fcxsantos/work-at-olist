from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from callapp import views

router = routers.DefaultRouter()
router.register(r'calls', views.CallViewSet)

urlpatterns = [
url(r'^$', views.CallList.as_view(), name='call_list'),
url(r'^bill', views.CallBill.as_view(), name='call_bill'),
url(r'^bill/(?P<phone>\d+)$', views.CallBill.as_view(), name='call_bill'),
url(r'^new', views.CallCreate.as_view(), name='call_new'),
url(r'^edit/(?P<pk>\d+)$', views.CallUpdate.as_view(), name='call_edit'),
url(r'^delete/(?P<pk>\d+)$', views.CallDelete.as_view(), name='call_delete'),
url(r'^end/(?P<pk>\d+)$', views.CallEnd.as_view(), name='call_end'),
url(r'^', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
