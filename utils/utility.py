import os 

# For color logs we are using this one 
startSequence="\033[90m"
endSequence="\033[0m"


def debugTool(text):
    if os.getenv("DEBUG")=="TRUE":
        print(f"{startSequence} {text} {endSequence}")
