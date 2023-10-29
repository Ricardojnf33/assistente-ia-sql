import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
