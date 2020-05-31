from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order

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

class OrderList(ListView):
    template_name = 'Order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs): # 로그인한 사용자의 주문만 조회하는 쿼리셋
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset

