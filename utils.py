import tiktoken

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
