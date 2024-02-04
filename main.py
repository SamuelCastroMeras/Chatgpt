from openai import OpenAI
import json
from dotenv import load_dotenv
x=load_dotenv()
API_KEY=os.enviroment("API_KEY")
client = OpenAI(api_key=os.enviroment.get("OPENAI_KEY",""))

messages = [
    {
        "role": "system", 
        "content": """
        Bienvenido al juego de BlackStories, donde tu sabras una historia y tendras que hacer que el usuario adivine la historia unicamente con preguntas de si o no. 
        Unicamente puedes responder si o no. Si la pregunta no se puede responder con un si o un no, dile al usuario que la pregunta no la puedes responder. 
        La historia que tienes que contar al jugador es: 
        Hay un hombre muerto en una sauna, esta tumbado, junto a el hay un termo. 
        El resto de la historia que el jugador tiene que descifrar a base de preguntas es que el hombre fue apuñalado con un carambano de hielo que su asesino habia introducido en un termo. 
        Poco despues del ataque, el carambano se derritio por el calor de la sauna, por lo que el arma del crimen nunca fue hallada. 
        Respondeme con un json, donde me devolveras el texto que el jugador recibira, con clave content y devuelveme una clave finished al final con un valor True si el usuario ha descubierto el caso, y un False si todavia esta intentando resolverlo.
        """
    },
]
print("Eres el jugador de un juego llamado Black Stories. ChatGPT va a tener una historia y tu tienes que descubrir lo que ha ocurrido. Para lograr descubrir lo que ha pasado tendras que hacer preguntas, y solo te podran responder con un si o un no.")
while True:
    messages.append({"role": "user", "content": input("Realiza tu pregunta: ")})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=messages
    )
    contenido_respuesta = response.choices[0].message.content
    messages.append({"role": "system", "content": contenido_respuesta})
    contenido_respuesta=json.loads(contenido_respuesta)
    print(contenido_respuesta["content"])
    if contenido_respuesta["finished"]:
        print("Muy bien, has resuelto el caso")
        break
