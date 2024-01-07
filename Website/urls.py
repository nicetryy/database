from django.contrib import admin
from django.urls import include, path

app_name = 'Website'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('', include('catalog.urls')),
]
