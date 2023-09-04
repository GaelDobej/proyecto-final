from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Salute_e_Vita import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Salute_cHome.urls'))
]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)