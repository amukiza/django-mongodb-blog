from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView,DetailView
from post.models import Posts
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.date_based',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(
        queryset = Posts.objects.all(),
        context_object_name="posts_list"),
        name='home'
    ),
    url(r'^post/(?P<slug>[a-zA-Z0-9-]+)/$', ListView.as_view(
        queryset=Posts.objects.all(),
        context_object_name="post"),
        name="post"
    )
)
