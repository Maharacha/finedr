"""finedr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views as authviews
from onsite.urls import router

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # API
    path('onsite/api/', include(router.urls)),
    path(
        'onsite/api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path(
        'onsite/api-token-auth/',
        authviews.obtain_auth_token
    )
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=True,
)

urlpatterns += i18n_patterns(
    path('onsite/', include('onsite.urls')),
    prefix_default_language=False,
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
