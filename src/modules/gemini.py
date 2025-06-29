from dotenv import load_dotenv
from os import environ
from google import genai


load_dotenv()


client = genai.Client()


def create_content(prompt):

    response = client.models.generate_content(

            model="gemini-2.5-flash",
            contents=prompt
    )

    return response.text


if __name__ == "__main__":

    print(create_content("Give an unhinged opinion about Java lovers"))
