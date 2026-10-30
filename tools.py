from datetime import datetime
import requests
from utils.utility import debugTool
import json 
def get_current_time():
    return datetime.now().strftime("%Y-%M -%d %H:%M:%S")


def get_weather_city(city):
    url=f"https://wttr.in/{city}?format=3"
    res=requests.get(url,timeout=10)
    res.raise_for_status(); # Yesla error raise garxa if error occur gara vana and will be catched by try and Exceptions
    return res.text  # there will be value in res.txt
#  TOOLS [{},{},{}]


def runTool(tool_call):
    func_name=tool_call.function.name
    func_args= {}
    
    try:
        func_arg=json.loads(tool_call.function.arguments or "{}")  # convert the json into dictionary 
        debugTool(f" Function Name: {func_name} Function Args :{func_arg}")
        fn=FUNCTION_NAME_TO_FUNCTION_MAP[func_name]
        result=fn(**func_arg)
    
                    
    except Exception as e:
                        result=f"Error while running the function {e}"

    return result
Tools=[
{
    "type":"function",
    "function":{
        "name":"get_current_time",
        "description":"Return the current Date and time as formatted String",
        "parameters":{"type":"object","properties":{}},
    },
},
{
  "type":"function",
      "function":{
          "name":"get_weather_city",
          "description":"Return the Weeather of Current time of Given place",
          "parameters":{
              "type":"object",
              "properties":{
                    "city":{
                        "type":"string",
                        "description":"City to get the requrest weather for"
                    }
              },
              "required":["city"]
         },
      },  
}
]


# When in future LLM Will take the name of functions from the functions name we need to acess the function

FUNCTION_NAME_TO_FUNCTION_MAP={
    "get_current_time":get_current_time,
    "get_weather_city":get_weather_city
}
