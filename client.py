from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="key",
)

command = '''
[11:53 pm, 8/8/2024] Anushka: Ha paper. A
[11:53 pm, 8/8/2024] Anushka: Apla
[11:53 pm, 8/8/2024] Kunal 🚀: Ha nahi ahe ha data science cha ahe aple ai and ml ahe
[11:54 pm, 8/8/2024] Anushka: Apan data science ghetle hote na
[11:55 pm, 8/8/2024] Kunal 🚀: Ha kale hote mi ani tu pan
[11:56 pm, 8/8/2024] Anushka: Br br
[11:57 pm, 8/8/2024] Kunal 🚀: Okk
[11:57 pm, 8/8/2024] Anushka: Udya lavkar ye
[11:57 pm, 8/8/2024] Kunal 🚀: Ha
[11:01 am, 9/8/2024] Anushka: Kiti time lagan
[11:01 am, 9/8/2024] Anushka: Tula
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Kunal who speaks marathi as well as english. You are from India and you are a coder. You analyze chat history and respond like Kunal"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
