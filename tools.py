from datetime import datetime
import requests

def get_current_time():
    return datetime.now().strftime("%Y-%M -%d %H:%M:%S")


def get_weather_city(city):
    url=f"https://wttr.in/{city}?format=3"
    res=requests.get(url,timeout=10)
    return res.text  # there will be value in res.txt
#  TOOLS [{},{},{}]

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
              }
         },
      },  
}
]


# When in future LLM Will take the name of functions from the functions name we need to acess the function

FUNCTION_NAME_TO_FUNCTION_MAP={
    "get_current_time":get_current_time,
    "get_weather_city":get_weather_city
}
