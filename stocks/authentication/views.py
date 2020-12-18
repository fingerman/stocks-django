from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views


class SignUpView(views.CreateView):
    form_class = UserCreationForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignInView(auth_views.LoginView):
    template_name = 'auth/signin.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
