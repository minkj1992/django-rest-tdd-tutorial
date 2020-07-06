from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from api.views import CreateView
from api.views import DetailsView


urlpatterns = {
    path('bucketlists/', CreateView.as_view(), name='bucketlist-list'),
    path('bucketlists/<int:pk>', DetailsView.as_view(), name='bucketlist-detail')
}

urlpatterns = format_suffix_patterns(urlpatterns) # json, html ...