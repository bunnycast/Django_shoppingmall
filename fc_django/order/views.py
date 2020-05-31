from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/prouct/' + str(form.product))

    def get_form_kwargs(self, **kwargs): # form을 생성할 때 인자값(kwargs)을 받는 함수
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw