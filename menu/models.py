from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.BooleanField(default=False)
    

    def __str__(self):
        return self.dish_name
class Order(models.Model):
    cutomer_name=models.CharField(max_length=100)
    # dish_name = models.CharField(max_length=100)
    dish_name = models.ManyToManyField(Dish, related_name='orders_as_dish')
    quantity = models.ManyToManyField(Dish, through='OrderQuantity', related_name='orders_as_quantity')
    status_choices = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='received')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    def __str__(self):
        return f"Order {self.pk}: {self.customer_name} ({self.status})"
# models.py

class OrderQuantity(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    dish_name = models.CharField(max_length=100)  # Add this field

    def __str__(self):
        return f"{self.quantity} x {self.dish_name} in Order #{self.order.id}"
  