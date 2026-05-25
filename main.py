import openai
from openai import OpenAI 
import os
from dotenv import load_dotenv
#Retry 
from tenacity import(
    retry,
    stop_after_attempt,
    wait_random_exponential
)

#Reduce tokens
import tiktoken 
#load .env
load_dotenv()

client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key=os.getenv("API_KEY"))

model = "GPT-5.4-mini"

messages = [
    {
        "role": "user",
        "content": "What is the core business means? Please return result in JSON format"
    }
]


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_response(model, messages):
    try: 
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"}
        )    
        return response.choices[0].message.content
    except openai.AuthenticationError as e:
        print(f"Authentication error: {e}")
        raise e 
    except openai.RateLimitError as e:
        print(f"Rate limit error: {e}")
        raise e 
    except openai.APIError as e:
        print(f"API error: {e}")
        raise e 
    except Exception as e:
        print(f"Unable to generate a response. Exception: {e}")
        raise e 

def count_tokens(model, messages):
    try:
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # Fallback to standard GPT-4 tokenizer for unknown model names
            encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(messages[0]['content']))
    except Exception as e:
        print(f"Error counting tokens: {e}")
        raise e 
    return num_tokens

print(get_response(model, messages))
print("token used: ", count_tokens(model, messages))