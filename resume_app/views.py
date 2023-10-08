from django.views import View
from django.shortcuts import render


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'landing_page.html', context)
