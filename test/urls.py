from django.conf.urls import url
from django.urls import path
from .newtest.test.view import TestView

urlpatterns = [
    path('', TestView.as_view(template_name='test.html'), name='test'),
]
