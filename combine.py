import json
import os
import subprocess
import sys

portals = {}
for fileName in [f for f in os.listdir("portals/")]:
    with open("portals/" + fileName, "r") as f:        
        portal = json.loads(f.read())
        portals[portal["id"]] = {
            "exists": portal["exists"],
            "location": portal["location"],
            "proofs": portal["proofs"]
        }

subprocess.call(["git", "clone", "git@github.com:EndYok/endyok.github.io.git"])

dataDir = "endyok.github.io/data"
if not os.path.exists(dataDir):
    os.makedirs(dataDir)
with open(dataDir + "/portals.json", "w") as f:
    f.write(json.dumps(portals))

sha = subprocess.check_output(["git", "log", "--format=\"%H\"", "-n", "1"]).replace("\"", "")
username = subprocess.check_output(["git", "log", "-1", "--pretty=format:'%an'"])
email = subprocess.check_output(["git", "log", "-1", "--pretty=format:'%ae'"])
os.chdir("endyok.github.io/")
subprocess.call(["git", "add", "."])
subprocess.call(["git", "-c", "user.name=" + username, "-c", "user.email=" + email, "commit", "-m", "fetch: EndYok/portallar@" + sha])
subprocess.call(["git", "push", "HEAD:source"])
    
