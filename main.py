from openai import OpenAI
import os
from audio import speech_to_text
import json
from dotenv import load_dotenv
from clase import Chat
load_dotenv()
client = OpenAI(api_key=os.environ.get("API_KEY", ""))


prompt1 = """
        Bienvenido al juego de BlackStories, donde tu sabras una historia y tendras que hacer que el usuario adivine la historia unicamente con preguntas de si o no. 
        Unicamente puedes responder si o no. Si la pregunta no se puede responder con un si o un no, dile al usuario que la pregunta no la puedes responder. 
        Un hombre fue apuñalado con un carambano de hielo que su asesino habia introducido en un termo.
        Poco despues del ataque, el carambano se derritio por el calor de la sauna, por lo que el arma del crimen nunca fue hallada. 
        Responde con un json. Se guardan las claves content y reason.
        Esta es la plantilla:
        {
            reason: "Porque has llegado a la conclusion de tu respuesta"
            relevante: "Responder true o false, dependiendo de si es relevante para resolver el caso o no"
            valid: "Responder true o false dependiendo de si puedes responder a esa pregunta con "si" o "no" o no puedes hacerlo"
            content: "true o false dependiendo de si la respuesta es un si o un no"

        }
        Ejemplo pregunta: "¿El hombre esta muerto?"
        {
            reason: "El hombre esta muerto segun la historia, por lo que la respuesta a la pregunta es sí"
            relevante: true
            valid: true
            content: true
        }
        Ejemplo pregunta: "¿El hombre es rubio?"
        {
            reason:"Esa informacíon es desconocida e irrelevante"
            relevante: false
            valid: true
            content: false
        }
        Ejemplo pregunta: "¿Como le han matado?"
        {
            reason:"No puedo responder a esa pregunta porque tendría que responder algo que no es un si o un no"
            relevante: true
            valid: false
            content: false
        }
        Ejemplo pregunta: "asdasdasdasd"
        {
            reason:"No puedo responder a esa pregunta porque no la entiendo"
            relevante: false
            valid: false
            content: false
        }
        """

prompt2 = """
        Tienes que recibir la información que el jugador ya ha descubierto y guardarlo, como si fuesen logros.
        Responde con un json. Se guardan en milestones de clave bool.
        Las milestones son estas:
            know_weapon (para cuando descubra que el arma es un carambano de hielo),
            know_wound(cuando sepa que ha seido apuñalado),
            know_death_cause (ha adivinado que la persona se ha desangrado),


        La respuesta tiene que ser un json con el siguiente formato:
        {
            reason: "Why the different milestones are discovered"
            know_weapon: false or true,
            know_wound: false or true,
            know_death_cause: false or true,
        }

        Ejemplo pregunta: Le han apuñalado?
        Response:
        {
            reason: "La respuesta demuestra que el hombre ha sido apuñalado"
            know_weapon: false,
            know_wound: true,
            know_death_cause: false,
        }
        Ejemplo pregunta: Se ha desangrado?
        Response:
        {
            reason: "La respuesta demuetra que el hombre se ha desangrado"
            know_weapon: false,
            know_wound: false,
            know_death_cause: true,
        }  
        Ejemplo pregunta: Le han matado con un carambano?
        Response:
        {
            reason: "La respuesta demuestra que el hombre ha sido asesinado con un carambano"
            know_weapon: true,
            know_wound: false,
            know_death_cause: false,
        }
        """

milestones = {"know_weapon": False,
            "know_wound": False,
            "know_death_cause": False
            }
completed_milestones = 0
print("Eres el jugador de un juego llamado Black Stories. ChatGPT va a tener una historia y tu tienes que descubrir lo que ha ocurrido. Para lograr descubrir lo que ha pasado tendras que hacer preguntas, y solo te podran responder con un si o un no.")
print(" Hay un hombre muerto en una sauna, esta tumbado, junto a el hay un termo. ")
response_finished = True
chat = Chat(prompt1)
chat2 = Chat(prompt2)
while True:
    input("Pulsa enter para grabar")
    pregunta = speech_to_text()
    print(pregunta)
    response1 = chat.send_message_json(pregunta)
    if not response1["valid"]:
        print("Tienes que hacer una pregunta de si o no")
        response_finished = True
        continue
    if not response1["relevante"]:
        print("Esa pregunta es irrelevante")
        response_finished = True
        continue

    if response1["content"]:
        print("Si.")
        response_finished = True
    else:
        print("No.")
        response_finished = True
    for valor in milestones.values():
        if valor:
            completed_milestones += 1
        else:
            continue
    if completed_milestones == 2:
        print("Muy bien, has resuelto el caso")
        break





# contenido_respuesta = response.choices[0].message.content
# contenido_respuesta2 = response_2.choices[0].message.content
# messages.append({"role": "system", "content": contenido_respuesta})
# message2.append({"role": "system", "content": contenido_respuesta2})
# contenido_respuesta = json.loads(contenido_respuesta)
# contenido_respuesta2 = json.loads(contenido_respuesta2)
# print(contenido_respuesta["content"])
