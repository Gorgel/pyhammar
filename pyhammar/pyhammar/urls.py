from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stromshammar.views.index', name='index'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^stadgar', 'stromshammar.views.stadgar', name='stadgar'),
    url(r'^styrelsen', 'stromshammar.views.styrelsen', name='styrelsen'),
    url(r'^vattengruppen', 'stromshammar.views.vattengruppen', name='vattengruppen'),
    url(r'^vagogront', 'stromshammar.views.vagogront', name='vagogront'),
    url(r'^lagindelning', 'stromshammar.views.lagindelning', name='lagindelning'),

    url(r'^boule', 'stromshammar.views.boule', name='boule'),
    url(r'^fest', 'stromshammar.views.fest', name='fest'),
    url(r'^fiske', 'stromshammar.views.fiske', name='fiske'),
    url(r'^golf', 'stromshammar.views.golf', name='golf'),

    url(r'^kontakt', 'stromshammar.views.kontakt', name='kontakt'),
    url(r'^historia', 'stromshammar.views.historia', name='historia'),
    url(r'^masonry', 'stromshammar.views.masonry', name='masonry'),
    url(r'^fragorosvar', 'stromshammar.views.fragorosvar', name='fragorosvar'),
    url(r'^forbattring', 'stromshammar.views.forbattring', name='forbattrings'),
    url(r'^license_bootstrap', 'stromshammar.views.license_bootstrap', name='license_bootstrap'),
    url(r'^license_lightbox', 'stromshammar.views.license_lightbox', name='license_lightbox'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)