from django.urls import include, re_path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

from wagtailautocomplete.urls.admin import \
    urlpatterns as autocomplete_admin_urls
from wagtailautocomplete.urls.public import \
    urlpatterns as autocomplete_public_urls

urlpatterns = [
    re_path(r'^admin/autocomplete/', include(autocomplete_admin_urls)),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^autocomplete/', include(autocomplete_public_urls)),
    re_path(r'', include(wagtail_urls)),
]
