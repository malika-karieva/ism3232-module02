# my_assistant.py
# Author: [Malika Karieva]

HANDOFF_WORDS = ["cancel", "refund", "change"]


class BakeryAssistant:
    """Assistant for Sweet Bakery orders."""

    def __init__(self, name, instructions, order_tracker):
        """Set up the assistant with rules, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.order_tracker = order_tracker
        self.history = []

    def respond(self, user_message):
        """Save messages, get a reply, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Pick a reply using simple rules."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't modify or cancel orders. I'm passing you to the manager."
        if "status" in text or "order" in text or "ready" in text:
            return self.status_reply(user_message)
        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. Ask me about your order status using your order number."
        return "I'm not sure how to help with that. I can check order statuses."

    def needs_human(self, text):
        """Check if request needs a human manager."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def status_reply(self, user_message):
        """Look up status using the order tool."""
        order_id = self.order_tracker.find_order_id(user_message)
        if order_id is None:
            return "Which order number? I can check orders like 101, 102, or 103."
        status = self.order_tracker.status_for(order_id)
        return f"Status for order {order_id}: {status}."
