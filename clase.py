from dotenv import load_dotenv
from openai import OpenAI
import os
import json
load_dotenv()


class Chat:
    def __init__(self, prompt):
        self.client = OpenAI(api_key=os.environ.get("API_KEY", ""))
        self.messages = [
            {
                "role": "system",
                "content": prompt
            },
        ]

    def send_message_json(self, msg: str,) -> dict[str: str]:
        self.messages.append({"role": "user", "content": msg})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=self.messages
        )
        respuesta = response.choices[0].message
        self.messages.append(respuesta)
        return json.loads(respuesta.content)