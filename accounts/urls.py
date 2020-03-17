from django.urls import path, re_path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^my-profile/$', views.ProfileDetailView.as_view(), name='my_profile'),
    re_path(r'^update-profile/$', views.update_profile, name='update_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='view_profile_with_pk'),
]
