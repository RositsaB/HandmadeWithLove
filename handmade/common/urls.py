from django.urls import path
from django.views.generic import TemplateView

urlpatterns = (
    path('404/', TemplateView.as_view(template_name='common/404_page.html'), name='404 page'),
    path('internal/', TemplateView.as_view(template_name='common/internal_error.html'), name='internal error'),
)