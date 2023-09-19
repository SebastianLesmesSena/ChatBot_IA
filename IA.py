# pip install openai 
import os
import openai
import config

openai.api_key = os.getenv(config.api_key1)
openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)