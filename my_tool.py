# my_tool.py
# Author: Malika Karieva


class OrderTracker:
    """Tool to check order status for Sweet Bakery."""

    def __init__(self, orders):
        """Save order data."""
        self.orders = orders

    def find_order_id(self, text):
        """Find an order number in text."""
        for order_id in self.orders:
            if order_id in text.lower():
                return order_id
        return None

    def status_for(self, order_id):
        """Get the status of an order."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None
