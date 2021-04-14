from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'