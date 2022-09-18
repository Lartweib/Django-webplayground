from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # Paths del auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/',include(profiles_patterns)),
    # Paths de messenger
    path('messenger/',include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
