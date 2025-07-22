# memory/short_term.py
import numpy as np

class ShortTermMemory:
    def __init__(self, max_turns=10):
        self.history = []
        self.max_turns = max_turns

    class ChatTurn:
        def __init__(self, user_msg: str, bot_msg: str):
            self.user_msg = user_msg
            self.bot_msg = bot_msg
            self.timestamp = np.datetime64('now')

    def add(self, user_msg: str, bot_msg: str):
        """Add a new chat turn"""
        chat_turn = ShortTermMemory.ChatTurn(user_msg, bot_msg)
        self.history.append(chat_turn)

        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def format(self) -> str:
        """Format the history for display"""
        return "\n".join([f"User: {ct.user_msg}\nAssistant: {ct.bot_msg}" for ct in self.history])

# Initialize the memory system when module is loaded
short_term_memory = ShortTermMemory()

if __name__ == "__main__":
    # Example usage
    short_term_memory.add("Hello, how are you?", "I'm good, thank you! How can I assist you today?")
    print(short_term_memory.format())
