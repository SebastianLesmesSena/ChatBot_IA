# pip install openai 
import openai
import config

# Configura tu clave de API
config.api_key1
openai.api_key = config.api_key1

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                             messages=[{"role":"user","content":"Hola \n ¿en que puede ayudarte este humilde ChatBot?"}])

print(response.choices[0].message.content)