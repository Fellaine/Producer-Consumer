from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import DeleteView, ListView

from .models import Order

# Create your views here.


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        current_user = self.request.user
        if self.request.user.is_anonymous:
            queryset = Order.objects.none()
        else:
            queryset = Order.objects.filter(employee=current_user)
        return queryset


class OrderDeleteView(DeleteView):
    model = Order
    # success_url = "/"

    def form_valid(self, form):  # proper way since django 4.0+
        order = self.get_object()
        # employee = f"{order.employee.username} {order.user.position}"
        employee = f"{self.request.user.username} {self.request.user.position}"
        time_date = datetime.now().strftime("%H:%M %d/%m/%Y")
        response = f"Order №{order.pk} - {order.task_id} named {order.name} \
                    was processed by {employee} at {time_date}"
        order.delete()
        return HttpResponse(response)


class OrderLoginView(LoginView):
    success_url = "/"


class OrderLogoutView(LogoutView):
    next_page = "/"  # so users aren't left at default admin logout page
