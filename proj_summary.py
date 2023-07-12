import openai
import json, os

this_file = os.path.dirname(__file__)
f = open(this_file + "/api_keys.json")
data = json.load(f)

api_key = data['api_key']
openai.api_key = api_key

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.75,
    )
    return response.choices[0].message["content"]

def processInfo():
    file = open("job.txt","r").read()

    prompt = f"""
        Your role is to make the text delimited by triple backticks stand out as an opening cover letter to a business.
        Write in the first person as if you are writing for a cover email.

        User input: ```{file}```
    """
    response = get_completion(prompt)
    
    print(response)
    inp = input("ok?")

processInfo()