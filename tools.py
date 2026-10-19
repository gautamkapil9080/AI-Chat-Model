from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%M -%d %H:%M:%S")


#  TOOLS [{},{},{}]

Tools=[{
    "type":"function",
    "function":{
        "name":"get_current_time",
        "description":"Return the current Date and time as formatted String",
        "parameters":{"type":"object","properties":{}},
    },
}]


# When in future LLM Will take the name of functions from the functions name we need to acess the function

FUNCTION_NAME_TO_FUNCTION_MAP={
    "get_current_time":get_current_time
}
