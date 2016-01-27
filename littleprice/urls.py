from django.conf.urls import url
from littleprice.views import index_view, supermercados_view, myaccount_view, login_view, registro_view, mis_productos_view, favoritos_view
from . import views

urlpatterns = [
	url(r'^$', index_view),
	url(r'^supermercados/$', supermercados_view),
	url(r'^myaccount/$', myaccount_view),
	url(r'^login/$', login_view),
	url(r'^registro/$', registro_view),
	url(r'^mis_productos/$', mis_productos_view),
	url(r'^favoritos/$', favoritos_view),

]