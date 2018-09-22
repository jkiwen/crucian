from os import environ
from dotenv import find_dotenv,load_dotenv

def load_settings():
    load_dotenv(find_dotenv())
    