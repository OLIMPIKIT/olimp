from django.conf.urls import url
#from . import views as s
from . import views
#from .core import views as s

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^faq/$', views.faq, name='faq'),

]