from openai import OpenAI
import os
import json
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.environ.get("API_KEY",""))

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
        resondeme con un json con clave content y valor la respuesta que le vas a dar al usuario.
        """
    },
]
message2 = [
    {
        "role": "system", 
        "content": """
        Tienes que recibir la información que el jugador ya ha descubierto y guardarlo, como si fuesen logros.
        Respondeme con un json, donde cada milestone tendra clave y valor, siendo la clave la milestone y el valor True o False, dependiendo de si ha sido completada.
        Esta es la lista de milestones: 

        know_weapon (para cuando descubra que el arma es un carambano de hielo), 
        know_wound(cuando sepa que ha seido apuñalado), 
        know_death_cause (ha adivinado que la persona se ha desangrado),
        finished (si el usuario ha adivinado el caso completo)
        recuerda devolverme un json
        
        """
    },
]
milestones={}
print("Eres el jugador de un juego llamado Black Stories. ChatGPT va a tener una historia y tu tienes que descubrir lo que ha ocurrido. Para lograr descubrir lo que ha pasado tendras que hacer preguntas, y solo te podran responder con un si o un no.")
while True:
    pregunta= input("Realiza tu pregunta: ")
    messages.append({"role": "user", "content":pregunta })
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=messages
    )

    message2.append({"role": "user", "content": pregunta })
    response_2 = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=message2
    )

    contenido_respuesta = response.choices[0].message.content
    contenido_respuesta2 = response_2.choices[0].message.content
    messages.append({"role": "system", "content": contenido_respuesta})
    message2.append({"role": "system", "content": contenido_respuesta2})
    contenido_respuesta=json.loads(contenido_respuesta)
    contenido_respuesta2=json.loads(contenido_respuesta2)
    print(contenido_respuesta["content"])
    if contenido_respuesta2["finished"]:
        print("Muy bien, has resuelto el caso")
        break

