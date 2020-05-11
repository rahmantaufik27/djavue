from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'index.html'