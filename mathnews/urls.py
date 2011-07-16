from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mathnews.views.home', name='home'),
    # url(r'^mathnews/', include('mathnews.foo.urls')),

    # django-cas
    (r'^accounts/login/$', 'django_cas.views.login'),
    (r'^accounts/logout/$', 'django_cas.views.logout'),

    # password
    (r'^auth/', include('django.contrib.auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^NJpgWbgpQli1mCEhxctqv1ekQ52KX04E6gouTnMWzWNe6bM377kh6w87fmgczqH/', 'mathnews.prodsys.views.cas_hack'),

    url(r'^login_hack/$', 'mathnews.prodsys.views.cas_hack_init'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
