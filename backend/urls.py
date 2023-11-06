from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.static import serve
from backendapp.users.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('backendapp.login.urls')),
    path('users/', include('backendapp.users.urls')),
    path('users/<int:pk>/', RegisterView.as_view()),
    path('', include('backendapp.urls')),
]
# urlpatterns += staticfiles_urlpatterns()
