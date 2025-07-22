from agent_system.agents.base import BaseAgent

from agent_system.memory.short_term import ShortTermMemory
# from memory.long_term import save_memory, search_memory

from agent_system.prompts.prompt_builder import build_prompt
from agent_system.shared.ollama_client import query_ollama

class AssistantAgent(BaseAgent):
    def __init__(self, short_term_window=5):
        self.st_mem = ShortTermMemory(max_turns=20)

    def handle_user_input(self, user_input: str) -> str:
        # 1. Retrieve long-term context
        # relevant_memories = search_memory(user_input)

        # 2. Compose prompt
        context = self.st_mem.format()
        
        # prompt = build_prompt(context, relevant_memories, user_input)
        prompt = build_prompt(context, user_input)

        # 3. Query LLM (stateless)
        response = query_ollama(prompt)

        # 4. Update memories
        self.st_mem.add(user_input, response)
        # save_memory("chat", f"User: {user_input} | Assistant: {response}")

        return response
