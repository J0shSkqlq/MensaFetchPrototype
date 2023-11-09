import json
from typing import List
from tokenize import String
from sys import argv

with open('shady.json', 'r') as f:
    shady = json.loads(f.read())

def getShadyString(str: String, fontDict: dict[List[str]]) -> String:
    output = ""
    for i in range(len(fontDict["A"])): #all chars should be the same height
        for char in str:
            if char in fontDict:
                output += fontDict[char][i]
        output += "\n"
    return output

if len(argv) > 1:
	print(getShadyString(argv[1], shady))
else:
	print(getShadyString("Test this font", shady))
            

'''
        |                |         _|         |     _)  _)  |     |                                                     |                                                    \     __ )   ___| __ \  ____| ____|  ___| |   |_ _|     | |  / |      \  |   \  |  _ \   _ \   _ \   _ \   ___| __ __| |   |\ \     /\ \        /  \  /\ \   /__  /
  _` |  __ \    __|   _` |   _ \  |     _  |  __ \   |   |  |  /  |  __ `__ \   __ \    _ \   __ \    _` |   __|   __|  __|  |   | \ \   / \ \  \   /  \  /  |   | _  /     _ \    __ \  |     |   | __|   |     |     |   |  |      | | /  |     |\/ |    \ | |   | |   | |   | |   |\___ \    |   |   | \ \   /  \ \  \   /     /  \   /    / 
 (   |  |   |  (     (   |   __/  _|   (   |  | | |  |   |    <   |  |   |   |  |   |  (   |  |   |  (   |  |    \__ \  |    |   |  \ \ /   \ \  \ /     <   |   |   /     ___ \   |   | |     |   | |     __|   |   | ___ |  |  \   | . \  |     |   |  |\  | |   | ___/  |   | __ <       |   |   |   |  \ \ /    \ \  \ /      \     |    /  
\__._| _.__/  \___| \__._| \___| _|   \__. | _| |_| _|   | _|\_\ _| _|  _|  _| _|  _| \___/   .__/  \__. | _|    ____/ \__| \__._|   \_/     \_/\_/   _/\_\ \__. | ___|  _/    _\ ____/ \____|____/ _____|_|    \____|_|  _|___|\___/ _|\_\_____|_|  _| _| \_|\___/ _|    \__\_\_| \_\_____/   _|  \___/    \_/      \_/\_/    _/\_\   _|  ____|
                                      |___/            _/                                    _|         _|                                                  ____/                                                                                                                                                                               

'''
