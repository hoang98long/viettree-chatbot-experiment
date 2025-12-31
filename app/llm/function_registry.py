FUNCTIONS = {
    "get_weather": {
        "description": "Get weather by city",
        "parameters": ["city"]
    }
}

def execute_function(name, args):
    if name == "get_weather":
        return f"Weather in {args['city']} is sunny 🌞"
