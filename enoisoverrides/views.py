from django.views.generic.list import ListView
from accounts.views import ProfileView
from accounts.models import TimtecUser


class EnoisProfileView(ProfileView):
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['portfolios'] = context['profile_user'].portfolio_set.all()[:4]
        return context


class TeachersView(ListView):
    context_object_name = 'teachers'
    template = 'teachers.html'

    def get_queryset(self):
        return TimtecUser.objects.all().filter(groups=2)
