import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_BOTS_Version_2.0")
BASE_URL = "https://newsapi.org/v2/top-headlines"

LANGUAGE = "en"
COUNTRY = "us"