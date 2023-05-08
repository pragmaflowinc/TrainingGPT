import os
from dotenv import load_dotenv
import openai

def main():
    load_dotenv()
    openai.organization = "org-uHgkJvi0fJy8D0BGR1BYSoqj"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.Model.list())

if __name__ == "__main__":
    main()