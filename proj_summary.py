import openai

openai.api_key = 'YOUR API KEY'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.75,
    )
    return response.choices[0].message["content"]

def processInfo():
    file = open("proj.txt","r").read()

    prompt = f"""
        Your role is to summarize the text delimited by triple backticks.
        Write in the first person as if you are writing for a CV.
        Use 200 words or less

        User input: ```{file}```
    """
    response = get_completion(prompt)
    
    print(response)
    inp = input("ok?")

processInfo()