from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', product, name='product_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
