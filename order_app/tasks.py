import random

from producer_consumer.celery import app

from .models import Employee, Order


@app.task
def make_order():
    random_user = random.choice(Employee.objects.all())
    order_number = Order.objects.count() + 1
    new_order = Order(
        task_id="1",
        name=f"Test name {order_number}",
        description="Test description",
        user=random_user,
    )
    new_order.save()
    return "Successfully added new order"
