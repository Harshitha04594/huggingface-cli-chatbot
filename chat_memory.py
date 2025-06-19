from collections import deque

class ChatMemory:
    def __init__(self, max_length=3):
        self.history = deque([], maxlen=max_length)

    def add_turn(self, user_input, bot_reply):
        self.history.append(f"User: {user_input}\nBot: {bot_reply}")

    def get_context(self):
        return "\n".join(self.history)
