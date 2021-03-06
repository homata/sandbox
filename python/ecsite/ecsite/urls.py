from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecsite.views.home', name='home'),
    # url(r'^ecsite/', include('ecsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^item/(?P<item_id>\d+)/$', 'ecsite.itempage.views.item_page_display'),
    url(r'^itemsearch', 'ecsite.itempage.views.item_search'),
    url(r'^cart', 'ecsite.itempage.views.do_cart'),
)
