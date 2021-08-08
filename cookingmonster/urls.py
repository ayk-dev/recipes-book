from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes_api.urls')),
    path('users/', include('users_auth.urls')),
    
]
