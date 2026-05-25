import openai_service 
from config import MODEL
from schemas import messages, function_definition
from openai_service import get_response, get_response_function_calling, get_response_content
from utils import count_tokens

if __name__ == "__main__":
    print("token used: ", count_tokens(MODEL, messages))
    response = get_response(MODEL, messages, function_definition)
    print("Response Content: ", get_response_content(response))
    print("Response Function Call: ", get_response_function_calling(response))