from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'framework.views.home', name='home'),
#    # url(r'^framework/', include('framework.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', direct_to_template, {'template': 'base.html'})
#)

core_urls = (
    url(r'^$', direct_to_template, {'template': 'base.html'}),
)

from framework.modules import get_modules_script

module_patterns = get_modules_script('urls')

urlpatterns = patterns('')

for pattern_file in module_patterns:
    pattern = getattr(pattern_file, 'urlpatterns', None)
    if pattern:
        urlpatterns += pattern

module_defined = {}

for t in urlpatterns:
    if hasattr(t, 'name') and t.name:
        module_defined[t.name] = True

core_defined = []

for u in core_urls:
    if not(hasattr(u, 'name') and u.name and (u.name in module_defined)):
        core_defined.append(u)

urlpatterns += patterns('', *core_defined)