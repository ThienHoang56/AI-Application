from config import MODEL
from schemas import messages, function_definition
from openai_service import get_response, get_response_function_calling
from utils import count_tokens

if __name__ == "__main__":
    print(get_response(MODEL, messages))
    print("token used: ", count_tokens(MODEL, messages))
    print(get_response_function_calling(MODEL, messages, function_definition))