from os.path import join, dirname
from dotenv import load_dotenv


def set_environments():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    # OR, the same with increased verbosity:
    load_dotenv(dotenv_path, verbose=True)