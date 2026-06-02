from datetime import datetime

def get_current_time():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tool_schema = {
    "name": "get_current_time",
    "description": "Returns the current date and time",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}
