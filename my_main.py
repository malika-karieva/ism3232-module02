# my_main.py
# Author: [Malika Karieva]

from my_assistant import BakeryAssistant
from my_tool import OrderTracker
from ollama_model import OllamaModel

INSTRUCTIONS = """You are Sam, an assistant for Sweet Bakery.
Answer in one short sentence.
Sweet Bakery is located at 123 Sugar Lane, downtown.
We are open daily from 7:00 am to 6:00 pm.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to the manager."""

ORDER_STATUSES = {
    "101": "ready for pickup",
    "102": "currently baking in the oven",
    "103": "out for delivery",
}

order_tracker = OrderTracker(ORDER_STATUSES)
model = OllamaModel("granite4.1:3b")
assistant = BakeryAssistant(
    "Sam",
    "You help customers of Sweet Bakery check their order status.",
    order_tracker,
    model,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
