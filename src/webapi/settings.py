from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    server_host = '127.0.0.1'
    server_port = 8000
    database_url = os.getenv('DEBUG')


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
