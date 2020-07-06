from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include

from api.views import CreateView


urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name='create'),
}

urlpatterns = format_suffix_patterns(urlpatterns) # json, html ...