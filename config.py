import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI Client
client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key=os.getenv("API_KEY")
)

# Configuration constants
MODEL = "GPT-5.4-mini"
