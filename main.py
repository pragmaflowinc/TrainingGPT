import os
import openai
openai.organization = "org-uHgkJvi0fJy8D0BGR1BYSoqj"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())