import os
from dotenv import load_dotenv
load_dotenv()


app_url = os.getenv("WEBAPP_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
