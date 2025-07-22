from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def handle_user_input(self, user_input: str) -> str:
        """Process input and return response."""
        pass

    def reset(self):
        """Optional: Reset memory or state."""
        pass

    def get_name(self) -> str:
        return self.__class__.__name__
