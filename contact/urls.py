from django.conf.urls import url
from .views import MessageAddView, MessageDetailView


urlpatterns = [
    url(r'^contact\/$', MessageAddView.as_view(), name='message-add'),
    ]