from more_itertools import chunked
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from portfolio.models import Portfolio
from .models import HomePage
from .serializers import HomePageSerializer


class HomePageViewSet(viewsets.ModelViewSet):
    model = HomePage
    serializer_class = HomePageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class HomePageView(DetailView):
    template_name = "homepage.html"

    def get_object(self):
        return HomePage.objects.get(pk=1)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['courses_slides'] = chunked(context['homepage'].promoted_courses.all(), 3)
        context['menthors_slides'] = chunked(context['homepage'].promoted_menthors.all(), 3)
        context['promoted_portfolios'] = Portfolio.objects.filter(
            home_published=True, status='published').order_by('-timestamp')[:8]
        return context
