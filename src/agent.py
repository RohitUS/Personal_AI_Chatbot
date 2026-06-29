from src.router import route

def chat(user_input):
    response = route(user_input)
    return response