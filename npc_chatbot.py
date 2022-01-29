import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nNPC:"
restart_sequence = "\nAdventurer: "

# get back story, and add it to the prompt
with open("backstory.txt", "r") as input_file:
    backstory = input_file.read()
prompt = backstory + "\nThe following is a conversation between an Adventurer and an NPC in the Divine City.\n"

# initial greeting
greeting = start_sequence + " greetings adventurer! how can i help you?"
print(greeting)
prompt += greeting

while True:
    # get user message
    message = input("Adventurer: ")
    prompt += restart_sequence + message + start_sequence

    # get response from api
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " NPC:", " Adventurer:"],
    )
    npc_message = response["choices"][0]["text"]
    print(f"NPC:{npc_message}")

    # add response to prompt
    prompt += npc_message + restart_sequence
