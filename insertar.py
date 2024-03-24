import os
import psycopg
from dotenv import load_dotenv
load_dotenv()


class Story:
    def __init__(self, story_name, short_story, long_story) -> None:
        self.story_name = story_name
        self.short_story = short_story
        self.long_story = long_story
class Milestones:
    def __init__(self, mile, why) -> None:
        self.mile = mile
        self.why = why

class Example:
    def __init__(self, question, reason, data) -> None:
        self.question = question
        self.reason = reason
        self.data = data

def insert_story() -> Story:
    historia_data = []
    story_name = input("Introduceme el nombre de la historia")
    short_story = input("Inserta la historia corta que el usuario leera")
    long_story = input("Introduce la historia completa que ChatGPT recibira")
    story= Story(story_name, short_story, long_story)
    return story


def insert_milestones() -> Milestones:
    list_milestones=[]
    cant_milestones = int(
        input("Introduce la cantidad de milestones que vas a querer"))
    for xaxa in range(cant_milestones):
        mile = input("Introduce tu milestone")
        list_milestones.append(mile)
        why= input("Introduce que significa cada milestone")

        milestones = Milestones(mile, why)
    return milestones


def insert_example(cant_milestones : int, list_milestones : list) -> Example:
    for xexe in range(cant_milestones):
        question = input("Introduce el ejempo de la pregunta que introduciria el usuario")
        for nene in range(cant_milestones):
            data = input("Introduce el resultado en bool que deberia de dar ",
                         list_milestones(nene), " : ")
        reason = input("Introduce la razon por lo que el codigo da eso")
    examples = Example(question, data, reason)
    return examples


# Connect to an existing database
with psycopg.connect(f'host={os.environ.get("host", "")} 
                     dbname={os.environ.get("db_name", "")} user={os.environ.get("pg_username", "")} 
                     password={os.environ.get("password", "")}') as conn:

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