from django.conf.urls import url
from littleprice.views import index_view, supermercados_view
from . import views

urlpatterns = [
	url(r'^$', index_view),
	url(r'^supermercados/$', supermercados_view),

]