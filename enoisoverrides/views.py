from accounts.views import ProfileView


class EnoisProfileView(ProfileView):
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['portfolios'] = context['profile_user'].portfolio_set.all()[:4]
        return context
