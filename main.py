# main.py
<<<<<<< HEAD
# Author: [Malika Karieva]

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)

bot = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant for Bayside Outfitters.",
    order_tool,
    stock_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
=======

# add sample inputs
from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

price, qty = 450.00, 3

total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"Total: {total:.2f}")
print(f"Requires Review: {review}")
print(f"Approval Tier: {tier}")
print(f"10% discount: {discounted_price:.2f}")
>>>>>>> 9cfa4b2e3dbf8e81908cefcb0b9782c0b77603fa
