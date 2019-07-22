from django.template.context_processors import csrf
from django.template.loader import render_to_string

from .forms import SwitchUserForm


def easy_login(request):
    context = {}
    context.update(csrf(request))
    context['form'] = SwitchUserForm(initial={'user': request.user.id})
    render_page = render_to_string("easy_login_form.html", context)

    return {"easy_login": render_page}
