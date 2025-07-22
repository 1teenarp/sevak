import requests
import json
import agent_system.agents.default_agent.agent as agent

URL = 'https://pokeapi.co/api/v2/pokemon/{POKE_NAME}'

def get_poke_info(poke_name):
    response = requests.get(URL.format(POKE_NAME=poke_name))
    # print('Fetching from', URL.format(POKE_NAME=poke_name))
    if response.status_code == 200:
        data = response.json()
        return {
            'pokemon': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [type['type']['name'] for type in data['types']],
        }
    else:
        print(f"Error fetching information about {poke_name}: {response.status_code}")
        return None 
    

def get_pokemon_prompt(poke_list):
    poke1_info = get_poke_info(poke_list[0])
    poke2_info = get_poke_info(poke_list[1])
    prompt = f"Given two pokemon information in JSON, can you tell which is powerful (estimate based on type, height and weight). Answer concisely but summarize your reasoning."\
            "<pokemon1>"+json.dumps(poke1_info)+"</pokemon1>" \
            "<pokemon2>"+json.dumps(poke2_info)+"</pokemon2>"
    return prompt
    

# print(get_poke_info('pikachu'))
if __name__ == "__main__":
    prompt = get_pokemon_prompt(input("enter 2 pokemon names separated by comma:\n").split(','))
    
    def_agent = agent.AssistantAgent(short_term_window=10)
    result = def_agent.handle_user_input(prompt)
    print(result)

    follow_up = input("Any follow up questions?\n:")
    follow_up_result = def_agent.handle_user_input(follow_up)
    print(follow_up_result)


