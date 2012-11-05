from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from Stud_finance.finance.views import *

urlpatterns = patterns('',
    ('^$', main_page),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^visitors/$', visitors),
    ('^del_user/([A-Za-z]+)/$', delete_user),
    (r'^get/([A-Za-z]+)/$', get),
    (r'^add_user/([A-Za-z]+)/$', add_user),
    (r'^add_to_user/([A-Za-z]+)/(.+)/(.+)/$', add_to_user),
    (r'^del_acc_from_user/([A-Za-z]+)/(.+)/(.+)/$', del_acc_from_user),

    # Example:
    # (r'^Stud_finance/', include('Stud_finance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
