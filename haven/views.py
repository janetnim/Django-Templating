from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
  def get(self, request, **kwargs):
    person = {
      'name': 'Sesame Developer',
      'gender': 'female',
      'company': 'Main Movers'
    }
    services = ['Packing', 'Moving', 'Arranging', 'Home decor']
    return render(request, "index.html", person)
