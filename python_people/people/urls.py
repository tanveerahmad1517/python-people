from django.conf.urls.defaults import patterns, url

from django.views.generic import DetailView

from people.views import  points, user_profile_upd, python_group_crud, python_users_bounded, profile_list, group_list
from people.models import PythonGroup, UserProfile

urlpatterns = patterns('',
    url(r'^kml/$', points, name='points'),
    #url(r'^profile/(?P<id>\d+)/$', user_profile_upd, name='userprofile-upd'),
    #url(r'^profile/list/$', ListView.as_view(queryset=UserProfile.objects.order_by("name"), template_name='people/userprofile_list.html',paginate_by=15) , name="user-profile-list"),
    url(r'^profile/list/$', profile_list, name="user-profile-list"),
    url(r'^profile/(?P<pk>\d+)/$', DetailView.as_view(model=UserProfile), name="user-profile"),
    url(r'^profile/form/$', user_profile_upd, name="user-profile-form"),

    url(r'^python_group/list/$', group_list, name='python-group-list'),
    url(r'^python_group/new/$', python_group_crud, name='python-group-crud'),
    url(r'^python_group/detail/(?P<pk>\d+)/$', DetailView.as_view(model=PythonGroup), name="python-group-detail"),
    url(r'^python_group/update/(?P<pk>\d+)/$', python_group_crud, name='python-group-crud'),
    url(r'^python_group/delete/(?P<pk>\d+)/$', python_group_crud, name='python-group-crud'),

    url(r'^list/bounded/(-?\d+\.\d+)/(-?\d+\.\d+)/(-?\d+\.\d+)/(-?\d+\.\d+)/$', python_users_bounded, name="python-user-list"),
)
