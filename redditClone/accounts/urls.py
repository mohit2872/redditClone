from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name="signup"),
    url(r'^login/', views.login_page, name="login_page"),
    url(r'^logout/', views.logout_page, name="logout_page"),
]
