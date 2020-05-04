import json
import os
import subprocess
import sys

if (len(sys.argv) != 1):
    sys.exit("Missing GitHub deploy key.")

sha = subprocess.check_output(["git", "log", "--format=\"%H\"", "-n", "1"]).replace("\"", "")
directory = "endyok.github.io/data"
portals = {}

for fileName in [f for f in os.listdir("portals/")]:
    with open("portals/" + fileName, "r") as f:        
        portal = json.loads(f.read())
        portals[portal["id"]] = {
            "exists": portal["exists"],
            "location": portal["location"],
            "proofs": portal["proofs"]
        }

subprocess.call(["git", "clone", "https://github.com/EndYok/endyok.github.io"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "fetch: EndYok/portallar@" + sha])

if not os.path.exists(directory):
    os.makedirs(directory)

with open(directory + "/portals.json", "w") as f:
    f.write(json.dumps(portals))
    
