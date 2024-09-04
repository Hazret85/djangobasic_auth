from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    CustomLogoutView,
    read_cookie_view,
    set_cookie_view,
    read_session_view,
    set_session_view,
)

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('cookie/read/', read_cookie_view, name='read_cookie'),
    path('cookie/set/', set_cookie_view, name='set_cookie'),

    path('session/read/', read_session_view, name='read_session'),
    path('session/set/', set_session_view, name='set_session'),
]
