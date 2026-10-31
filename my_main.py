# my_main.py
# Author: [Malika Karieva]

from my_assistant import BakeryAssistant
from my_tool import OrderTracker

ORDER_STATUSES = {
    "101": "ready for pickup",
    "102": "currently baking in the oven",
    "103": "out for delivery",
}

order_tracker = OrderTracker(ORDER_STATUSES)
assistant = BakeryAssistant(
    "Sam",
    "You help customers of Sweet Bakery check their order status.",
    order_tracker,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
