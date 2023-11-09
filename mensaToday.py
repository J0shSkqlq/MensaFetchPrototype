from math import fabs
from re import ASCII
import requests
import datetime
import sys 
import re

def PrettyPrintJson(data) -> None:
    output = ""
    for item in data:
        output += "-----------\n"  # Separator between dictionary items
        for key, value in item.items():
            if isinstance(value, dict):  # Check if the value is a nested dictionary
                output += f"\033[1m{key}:\033[0m\n"  # Bold key
                for nested_key, nested_value in value.items():
                    output += f"  {nested_key}: {nested_value}\n"
            else:
                output += f"\033[1m{key}:\033[0m \033[33m{value}\033[0m\n"
    print(output)

lastparam = sys.argv[-1]

today = datetime.datetime.today().strftime("%Y-%m-%d")
matrixlat = 51.034128
matrixlon = 13.733597
mensaIds = {
    '-matrix': 80,
    '-zelt': 78
}
asciiArts = { 80 : ''' 
\033[36m----------------------------------------------------------------------------
|   \  |                                  \  |         |         _)        |
|  |\/ |   _ \  __ \    __|   _` |       |\/ |   _` |  __|   __|  |  \  /  |
|  |   |   __/  |   | \__ \  (   |       |   |  (   |  |    |     |    <   |
| _|  _| \___| _|  _| ____/ \__._|      _|  _| \__._| \__| _|    _| _/\_\  |
----------------------------------------------------------------------------\033[0m
''',
             78 : ''' 
\033[36m------------------------------------------------------------------------------------------------
| __  /       |  |     ___|        |      |                                 |                  |
|    /   _ \  |  __| \___ \   __|  __ \   |   _ \    _ \   __|   __|   __|  __ \    _ \  __ \  |
|   /    __/  |  |         | (     | | |  |  (   |   __/ \__ \ \__ \  (     | | |   __/  |   | |
| ____|\___| _| \__| _____/ \___| _| |_| _| \___/  \___| ____/ ____/ \___| _| |_| \___| _|  _| |
------------------------------------------------------------------------------------------------\033[0m          
'''
}
id = mensaIds[lastparam] if lastparam in mensaIds else mensaIds['-matrix']
url="https://openmensa.org/api/v2"
#endpoint = f"{url}/canteens?near[lat]={matrixlat}&near[lng]={matrixlon}"
endpoint = f"{url}/canteens/{id}/days/{today}/meals"
meals = requests.request("GET", endpoint).json()
dataToPrint = [{"name": re.sub(r" \(.*?\)", "", meal["name"]), "price": meal["prices"]["students"]} for meal in meals]
print(asciiArts[id])
PrettyPrintJson(dataToPrint)
