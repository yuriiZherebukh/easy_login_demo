from django.conf.urls import url
from django.contrib import admin
from easy_login_demo.home.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home")
]
