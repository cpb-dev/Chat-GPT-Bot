import openai, os, json

this_file = os.path.dirname(__file__)
f = open(this_file + "/api_keys.json")
data = json.load(f)
api_key = data['api_key']

openai.api_key = api_key
messages = [ { "role": "system", "content": "You are a intelligent assistant."} ]

while True:
    message = input("User: ")
    if message:
        messages.append(
            {"role": "user", "content": message}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages
            )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": "reply"})
