from django.urls import path

from django.views.generic.base import TemplateView

urlpatterns = [
  # other patterns here
  path('hello-webpack/', TemplateView.as_view(template_name='hello_webpack.html'))
]