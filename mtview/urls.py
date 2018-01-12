from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^videos/$', views.videos, name='videos'),
    url(r'^video/(?P<video>[\w|\W]+)/$', views.video, name='video'),
    url(r'^login/$', auth_views.login, {'template_name': 'mtview/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'mtview/logout.html', 'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^roster/$', views.roster, name='roster'),
    url(r'^schoolstore/$', views.schoolstore, name='schoolstore'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^budgets/$', views.budgets, name='budgets'),
    url(r'^videopayment/$', views.videopayment, name='videopayment'),
    url(r'^uploadvideos/$', views.uploadvideos, name='uploadvideos'),
]
