from ollama import chat, ChatResponse


def summarize_text(input_text):

    prompt = f"""
    Make a clean resume of this video's transcript. If it's in portuguese, return the resume in portguese.
    Texto:
    \"\"\"
    {input_text}
    \"\"\"
    """

    response: ChatResponse = chat(model='mistral', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    
    print(response['message']['content'])