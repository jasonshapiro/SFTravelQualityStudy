from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^$', 'info.views.index'),
    (r'^about/$', 'info.views.about'),
    (r'^instructions/$', 'info.views.instructions'),
    (r'^team/$', 'info.views.team'),
    (r'^usingmuni/$', 'info.views.new_to_muni'),
    (r'^signup/$', 'info.views.signup'),
    (r'^survey/$', 'info.views.survey'),
    (r'^contact/$', 'info.views.contact'),
    (r'^install_instructions/$', 'info.views.install'),
    (r'^participation_instructions/$', 'info.views.participation'),
    (r'^widget_instructions/$', 'info.views.widget'),
    
    # Examples:
    # url(r'^$', 'SF_Traveler.views.home', name='home'),
    # url(r'^SF_Traveler/', include('SF_Traveler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
