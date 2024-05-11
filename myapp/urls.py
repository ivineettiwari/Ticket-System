from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import view

urlpatterns = [
    path('ticket', view.ticket ,name = 'ticket'),
    # re_path('load_edit_form/<pk>/', view.edit_view, name='load_edit_form')
] 

# Serve static files during development with DEBUG=False
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)