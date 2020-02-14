from dotenv import load_dotenv
from pathlib import Path
import os


class Settings:
	
	env_path = Path('.') / '.env'

	load_dotenv(dotenv_path = env_path)

	SERVER = os.getenv("SERVER")
	DATABASE = os.getenv("DATABASE")
	USERNAME = os.getenv("USERNAME")
	SECRET = os.getenv("SECRET")

