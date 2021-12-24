import json
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from pages.models import Parish, Mass

# Create your views here.
class KevinsPageView(TemplateView):
    template_name = 'stkevins/stkevinshome.html'

"""
def parish_view(request, *args, **kwargs):
    query_results = Parish.objects.get(pk=1)
    parish = {'query_results': query_results}
    return render(request, "stkevins/stkevinshome.html", parish)



class MassesTemplateView(TemplateView):
    template_name = 'stkevins/countdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = json.dumps(
            [
                {
                    'times': obj.start_time.isoformat()
                }
                for obj in Mass.objects.all()
            ]
        )

        return context
"""