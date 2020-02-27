from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from django.views.generic import FormView, View, ListView

from authentication.forms import LoginForm
from portal.models import Article


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'login.html', {'form', form})


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(LoginView, self).get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return super().post()

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request,
                            username=username,
                            password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        return redirect('/')


class LogoutView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(is_deleted=False)
    paginate_by = 1
