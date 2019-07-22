from django.conf.urls import url, include
from django.contrib import admin
from easy_login_demo.home.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^easy_login/', include('easy_login_demo.easy_login.urls', namespace='easy-login')),
]
