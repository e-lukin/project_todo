from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('task/', include('task.urls')),
    path('admin/', admin.site.urls),
]
