from django.urls import path, re_path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    #re_path(r'^my-profile/$', views.ProfileDetailView.as_view(), name='my_profile'),
    re_path(r'^update-profile/$', views.update_profile, name='update_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$',
            views.ProfileDetailView.as_view(), name='view_profile_with_pk'),
    re_path(r'^change-password/$', views.MyPasswordChangeView.as_view(),
            name='change_password'),
    re_path(r'^password_reset/$', views.MyPasswordResetView.as_view(),
            name='password_reset'),
    re_path(r'^password_reset/done/$',
            views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', views.MyPasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
]
