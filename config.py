from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY', '')
    AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', '')
    AZURE_OPENAI_ASSISTANT_ID: str = os.getenv('AZURE_OPENAI_ASSISTANT_ID', '')
    SOURCE_TYPE: str = os.getenv('SOURCE_TYPE', 'local')
    SOURCE_PATH: str = os.getenv('SOURCE_PATH', './data')
