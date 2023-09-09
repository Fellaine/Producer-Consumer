from django.views.generic import DeleteView, ListView

from .models import Order

# Create your views here.


class OrderListView(ListView):
    model = Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/"
