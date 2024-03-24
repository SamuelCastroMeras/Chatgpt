import os
import psycopg
from dotenv import load_dotenv
load_dotenv()
def insert_story() -> list:
    historia_data=[]
    story_name=input("Introduceme el nombre de la historia")
    short_story=input("Inserta la historia corta que el usuario leera")
    long_story=input("Introduce la historia completa que ChatGPT recibira")
    historia_data.append(story_name) , historia_data.append(short_story) , historia_data.append(long_story)
    return historia_data


def insert_milestones():
    milestones=[]
    cant_milestones=int(input("Introduce la cantidad de milestones que vas a querer"))
    for x in range(cant_milestones):
        mile=input("Introduce tu milestone")
        milestones.append(mile)
        mile=""
    return milestones


def insert_example(milestones : list) -> tuple:
    examples=[]
    milestones_values=[]
    for x in range(len(milestones)):
        question=input("Introduce el ejempo de la pregunta que introduciria el usuario")
        milestones_values.append(question)
        for n in range(len(milestones)):
            data=input("Introduce el resultado en bool que deberia de dar ",milestones(n)," : ")
            milestones_values.append(data)
            data=""
        reason=input("Introduce la razon por lo que el codigo da eso")
        milestones_values.append(reason)
        reason=""
        examples.append(milestones_values[])
    return examples


# Connect to an existing database
with psycopg.connect(f'dbname={os.environ.get("db_name", "")} user=f{os.environ.get("username", "")} password=f{os.environ.get("password", "")} db_name=f{os.environ.get("db_name", "")}') as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        story_name,long_story,short_story = insert_story()
        cur.execute(
            "INSERT INTO samu (Historia) VALUES (%s, %s, %s)",
            (story_name,long_story,short_story))

        cur.execute("SELECT * FROM samu")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()