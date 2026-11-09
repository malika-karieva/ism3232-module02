from mock_model import MockModel
from my_assistant import BakeryAssistant
from my_tool import OrderTracker


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    tracker = OrderTracker({"101": "ready for pickup", "103": "out for delivery"})
    return BakeryAssistant("Sam", "Be polite.", tracker, MockModel())


def test_order_status_question_uses_the_tool():
    assistant = make_assistant()
    reply = assistant.respond("What is the status of order 101?")
    assert reply == "Status for order 101: ready for pickup."


def test_question_without_a_known_order_asks_for_one():
    assistant = make_assistant()
    assert "Which order number?" in assistant.respond(
        "What is the status of order 999?"
    )


def test_cancellation_request_goes_to_a_human():
    assistant = make_assistant()
    assert "manager" in assistant.respond("Please cancel order 101")


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is your favorite cake flavor?")


def test_history_grows_by_two_each_turn():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What is order 103 status?")
    assert len(assistant.history) == 4
