from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tabledata/$', views.TableView.as_view(), name='tabledata'),

]
