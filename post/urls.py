from django.conf.urls import patterns, include, url


urlpatterns = patterns('post.views',
    url(r'^$', 'list_view', name='post_list'),
    url(r'^category/(?P<slug>[a-zA-Z0-9\-]+)', 'list_view', name='category_list'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)', 'single_view', name='post_single')
)