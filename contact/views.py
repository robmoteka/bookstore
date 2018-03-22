from django.shortcuts import render
from .models import Message
from django.views.generic import DetailView, FormView
from .forms import MessageForm, ContactForm


class MessageDetailView(DetailView):
    model = Message


class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/contact/contact'

    # def form_valid(self, form):
    #     form.save()
    #     return super(MessageAddView, self).form_valid(form)
