# my_assistant.py
# Author: [Malika Karieva]

HANDOFF_WORDS = ["cancel", "refund", "change"]


class BakeryAssistant:
    """Assistant for Sweet Bakery orders. Rules handle order status and handoffs. A model handles the rest."""

    def __init__(self, name, instructions, order_tracker, model):
        """Set up the assistant with rules, tool, model and history."""
        self.name = name
        self.instructions = instructions
        self.order_tracker = order_tracker
        self.model = model
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
        return self.model_reply()
        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. Ask me about your order status using your order number."
        return "I'm not sure how to help with that. I can check order statuses."

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

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
