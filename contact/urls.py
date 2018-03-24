from django.conf.urls import url
from .views import MessageAddView, MessageDetailView



app_name = "contact"


urlpatterns = [
    url(r'^form\/$', MessageAddView.as_view(), name='message-add'),
    ]