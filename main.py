import openai
from openai import OpenAI 

#Retry 
from tenacity import(
    retry,
    stop_after_attempt,
    wait_random_exponential
)
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key=os.getenv("API_KEY"))

try: 
    response = client.chat.completions.create(
        model="GPT-5.4-mini",
        messages=[
            {   "role": "user",
                "content" : "What is the core business means? Please return result in JSON format"    
            }
        ],
        response_format={"type": "json_object"}
    ) 
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
    print(f"Authentication error: {e}")
    pass
except openai.RateLimitError as e:
    print(f"Rate limit error: {e}")
    pass
except openai.APIError as e:
    print(f"API error: {e}")
    pass
except Exception as e:
    print(f"Unable to generate a response. Exception: {e}")