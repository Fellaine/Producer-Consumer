from django.views.generic import DeleteView, ListView

from .models import Order

# Create your views here.


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        current_user = self.request.user
        if self.request.user.is_anonymous:
            queryset = Order.objects.none()
        else:
            queryset = Order.objects.filter(user=current_user)
        return queryset


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/"
