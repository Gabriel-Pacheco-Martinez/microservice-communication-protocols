import os
from dotenv import load_dotenv

load_dotenv()  # load .env file

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a:8000")  # Docker maps port to host port