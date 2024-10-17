# Use a pipeline as a high-level helper
from chroma import ChromaInterface
from dotenv import load_dotenv
from openai import OpenAI
import os


class Chatbot:
    def __init__(self):
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.chroma = ChromaInterface()
        self.chroma.upsert_chunks()

    def chat(self, query: str) -> str:
        client = OpenAI(api_key=self.OPENAI_API_KEY)

        results = self.chroma.query(query)

        system_prompt = f"""
        You are a helpful assistant who answers questions based on the Bitcoin whitepaper. You only answer based on knowledge contained in the documentation and do not provide personal opinions.
        
        If you don't know the answer, you can say "I don't know."
        
        You are given the documentation: {str(results['documents'])}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
        )

        return response.choices[0].message.content


chatbot = Chatbot()
query = input("\nAsk the Bitcoin chatbot a question!\n")
response = chatbot.chat(query)
print(response)
