
# def build_prompt(short_term_ctx, long_term_memories, user_input):
#     mem_block = "\n".join([f"[Memory]: {m[1]}" for m in long_term_memories])
#     return f"""{short_term_ctx}
# {mem_block}

# User: {user_input}
# Assistant:"""


def build_prompt(short_term_ctx, user_input):
    return f"""{short_term_ctx}
    
User: {user_input}
Assistant:"""
