from django.conf.urls import url

from .views import EasyLoginView

urlpatterns = [
    url('^easy_login_change/$',  EasyLoginView.as_view(), name='easy-login-change')
]
