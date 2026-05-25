import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
from config import client

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

def get_response_function_calling(model, messages, function_definition):
    try: 
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=function_definition,
            tool_choice={"type": "function", "function": {"name": "get_properties"}}
        )    
        return response.choices[0].message.tool_calls[0].function.arguments
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
